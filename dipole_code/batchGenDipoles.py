# IMPORTS
import datetime
import subprocess
import sys
import os
import time
from datetime import datetime
from genDipoles import buildSphere
from numpy import *

# CONSTANTS
# If SGE Cluster - create job to be run via `qsub`
SGE_ENV = False
# System type affects where the correct ADDA executable is found
LINUX_ENV = True


# Execute command and yield output as it is received
def execute(cmd):
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)

# def gen_sphere(dpl, grid, x, y, z):
#     return buildSphere(dpl, grid, x, y, z)

def write_dipoles(dipoles, filename, new_file=True):
    # Open file
    f = open(filename, 'w+')
    for d in dipoles:
        f.write(str(int(d[0])) + ' ' + str(int(d[1])) + ' ' + str(int(d[2])) + '\n')
    f.close()

# Run ADDA and grab output as it runs
def adda_run(monomers, grid='30', dplSize='10', filename='./output/runs/outputDipoleXYZ.txt', overlap='0.5', monomer_radius=15):
    """shift = round(float(grid) - float(overlap) * float(grid))
    new_overlap = float(grid) - float(shift) / float(grid)
    print('OVERLAP OF ' + overlap + ' ROUNDED TO ' + str(new_overlap))
    print('SHIFT ' + str(shift))"""

    dipole_radius = round(float(dplSize) / float(grid))
    print('grid:{}'.format(grid))
    print('dplSize:{}'.format(dplSize))
    print('dipole radius:{}'.format(dipole_radius))
    print('monomer radius:{}'.format(monomer_radius))

    dipoles = []
    for m in monomers:
        print('monomer: {}'.format(m))
        # dipoles = list(set(dipoles + buildSphere(dplSize, grid, m[0], m[1], m[2])))
        # Get dipoles for monomer
        monomer_dipoles = buildSphere(dplSize, grid, m[0], m[1], m[2])
        # Insert spacing into dipoles so they fill proper volume regardless of dipole size
        monomer_dipoles = space_dipoles(monomer_dipoles, monomer_radius, dipole_radius, m[0], m[1], m[2])
        # Append monomer dipoles to entire array of dipoles
        # NOTE: This doesn't scale well, consider outputting to a file
        dipoles += monomer_dipoles
        # Remove duplicates
        dipoles = list(set(dipoles))

    write_dipoles(dipoles, './output/runs/dipole_output_grid' + grid + '_dplsize' + dplSize + '.txt')

    # Run ADDA
    cmdRunADDA = []
    addaExec = '../adda/src/seq/adda' if LINUX_ENV else '../adda/win64/adda.exe' # TODO: depending on var change which adda src is ran (seq,mpi,ocl)
    if SGE_ENV:
      cmdSGE = addaExec + ' -m 1.85 0.71 -lambda 0.55 -shape read ' + filename + ' -dpl ' + dplSize + ' -dir ./output/runs/dipole_output_grid' + grid + '_dplsize' + dplSize
      # cmdRunADDA = ['echo', "'" + cmdSGE + "'", '>', 'sge_job.sh']
      f = open('sge_job.sh', 'w')
      f.write(cmdSGE)
      f.close()
      # qsub command is for an SGE environment; -V = use shell var; -b = bin (y) or exec (n); -cwd = execute in same dir as qsub call
      cmdRunADDA = ['qsub', '-V', '-b', 'n', '-cwd', './sge_job.sh']
    else:
      cmdRunADDA = [addaExec, '-m', '1.85', '0.71', '-lambda', '0.55', '-shape', 'read', filename, '-dpl', dplSize, '-dir', './output/runs/dipole_output_grid' + grid + '_dplsize' + dplSize]
    
    adda_output(cmdRunADDA)

def adda_output(cmdRunADDA):
  # Init formatted output file
  file_output = open('./output/outputExcelParsed.txt', 'w')
  s1 = ''
  s2 = ''
  t0 = -1

  if SGE_ENV:
    # SGE... - read program output from file once sge job is done
    # TODO: Need job id, need to periodically check the status of the job
    job_id = 'job id here'
    for output in execute(cmdRunADDA):
      print('output={}'.format(output))
      if 'Your job ' in output:
        start = output.index('Your job ') + 9
        end = output.index(' (')
        job_id = output[start:end]
    print('job id: {}'.format(job_id))
    output_filename = 'sge_job.sh.o' + job_id
    print('output_filename={}'.format(output_filename))

    # wait until sge job done - TODO: improve this - use qstat instead of checking the existence of a file
    job_running = True
    while job_running:
      for output in execute(['qstat', '-j', job_id]):
        print('qstat output: {}'.format(output))
      break
      time.sleep(5)
      print('SGE job not done - waiting 5s to try again..')

    return # TODO: REMOVE

    adda_output = ''
    try:
      adda_output = open(output_filename)
    except Exception as e:
      print('Could\'t open adda output, error={}'.format(e))
      return

    for line in adda_output:
      print('sge output: {}'.format(line))
      s1, s2, t0 = process_adda(line, s1, s2, t0)
    adda_output.close()
  else:
    for output in execute(cmdRunADDA):
      # Push output to console
      print(output, end="")

      s1, s2, t0 = process_adda(line, s1, s2, t0)

    # Time to execute
    # t1 = time.time()
    s1 += '\t' # str(t1 - t0)[:9] + '\t'

    # Write to file
    file_output.write(s1 + '\t' + s2 + '\n')

def process_adda(output, s1, s2, t0):
  print('')
  # Run #
  if ('all data is saved in' in output):
      value = output[25:28]
      s1 += value + '\t'

  # Date + ADDA memory usage
  if ('Total memory usage' in output):
      value = output.split()[-2:]
      s1 += datetime.now().strftime("%m/%d/%Y") + '\t'
      s1 += value[0] + '\t'

  # Num dipoles
  if ('Total number of occupied dipoles' in output):
      value = output.split()[-1:]
      s1 += value[0] + '\t'

  # ADDA light data
  if ('Cext' in output or 'Qext' in output or 'Cabs' in output or 'Qabs' in output):
      value = output.split()[-1:]
      s2 += value[0] + '\t'

  return s1, s2, t0

def readExcelInput(filename='./input/inputExcelRuns.txt'):
    # Read excel data input
    f = open(filename)
    try:
         text = f.read()
    finally:
         f.close()
    text = text.split()
    dplSize = []
    grid = []
    overlap = []
    for number in range(3,len(text),3):
        dplSize.append(text[number])
        grid.append(text[number+1])
        overlap.append(text[number+2])

    return dplSize, grid, overlap

# Shift monomer centers to all be positive
def operate_shift(monomers, radius):
    minx=radius
    miny=radius
    minz=radius
    # finding minmum x y z
    for m in monomers:
        minx = min(minx, m[0])
        miny = min(miny, m[1])
        minz = min(minz, m[2])
    # shifting
    for m in monomers:
        m[0] = round(m[0] - minx + radius)
        m[1] = round(m[1] - miny + radius)
        m[2] = round(m[2] - minz + radius)
    return monomers

# Space dipoles depending on the size of the dipoles (so they always fill the same volume)
# NOTE: run this step before the monomers are appended together
# TODO: use pandas: dipoles *= spacing
# TODO: This should probably be in the genDipoles file
def space_dipoles(dipoles, monomer_radius, dipole_radius, x_offset, y_offset, z_offset):
    spacing = monomer_radius * 4 / dipole_radius
    print('spacing: {}'.format(spacing))
    new_dipoles = []
    for d in dipoles:
        x = d[0]
        y = d[1]
        z = d[2]
        x += int((x - x_offset) * spacing)
        y += int((y - y_offset) * spacing)
        z += int((z - z_offset) * spacing)
        new_dipoles.append((x,y,z))
        
    return new_dipoles

# Read fracmap output file
def read_fracmap(filename):
    print('Reading fracmap output from file: {}'.format(filename))
    f = open(filename)
    try:
        text = f.read()
    except:
        print('ERROR: Could not open fracmap output file')
        return
    finally:
        f.close()
    text = text.split('\n')
    read_centers = False
    monomers = []
    monomer_radius = 0
    for line in text:
        if not read_centers and 'a:' in line:
            monomer_radius = float(line.split()[1])
        elif read_centers and len(line) == 0:
            break

        if read_centers:
            x,y,z = line.split()
            monomers.append([float(x), float(y), float(z)])

        if line == 'X Y Z':
            read_centers = True

    return monomer_radius, monomers

# program start
def main():
    # Read input parameters
    dplSize, grid, overlap = readExcelInput()

    print('dplSize: {}\ngrid: {}\noverlap: {}'.format(dplSize, grid, overlap))

    # Read FracMAP input
    monomers = []
    monomer_radius = 0
    if len(sys.argv) > 1:
        monomer_radius, monomers = read_fracmap(sys.argv[1])

    # Shift monomers to lose any negative values
    monomers = operate_shift(monomers, monomer_radius)

    # Iterate over run parameters
    for k in range(len(dplSize)):
        adda_run(monomers,
                grid[k],
                dplSize[k],
                './output/runs/dipole_output_grid' + str(grid[k]) + '_dplsize' + str(dplSize[k]) + '.txt',
                overlap[k],
                monomer_radius)


main()
