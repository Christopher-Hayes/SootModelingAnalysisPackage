from sys import argv

f_in = open(argv[1], "r")
f_out = open(argv[1] + '.out', "w")

# by line
lines = f_in.readlines()
for y in range(9,len(lines)):
    # by int
    vals = lines[y].split(' ')
    for x in range(0,3):
        f_out.write(str(round(float(vals[x]))))
        if x < 2:
            f_out.write(" ")
    f_out.write("\n")
