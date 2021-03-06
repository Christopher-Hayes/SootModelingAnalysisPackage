# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/chris/surf/fracmap/libigl/tutorial

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/chris/surf/fracmap/libigl/tutorial/build

# Include any dependencies generated for this target.
include embree/common/simd/CMakeFiles/simd.dir/depend.make

# Include the progress variables for this target.
include embree/common/simd/CMakeFiles/simd.dir/progress.make

# Include the compile flags for this target's objects.
include embree/common/simd/CMakeFiles/simd.dir/flags.make

embree/common/simd/CMakeFiles/simd.dir/sse.cpp.o: embree/common/simd/CMakeFiles/simd.dir/flags.make
embree/common/simd/CMakeFiles/simd.dir/sse.cpp.o: /home/chris/surf/fracmap/libigl/external/embree/common/simd/sse.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/chris/surf/fracmap/libigl/tutorial/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object embree/common/simd/CMakeFiles/simd.dir/sse.cpp.o"
	cd /home/chris/surf/fracmap/libigl/tutorial/build/embree/common/simd && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/simd.dir/sse.cpp.o -c /home/chris/surf/fracmap/libigl/external/embree/common/simd/sse.cpp

embree/common/simd/CMakeFiles/simd.dir/sse.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/simd.dir/sse.cpp.i"
	cd /home/chris/surf/fracmap/libigl/tutorial/build/embree/common/simd && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/chris/surf/fracmap/libigl/external/embree/common/simd/sse.cpp > CMakeFiles/simd.dir/sse.cpp.i

embree/common/simd/CMakeFiles/simd.dir/sse.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/simd.dir/sse.cpp.s"
	cd /home/chris/surf/fracmap/libigl/tutorial/build/embree/common/simd && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/chris/surf/fracmap/libigl/external/embree/common/simd/sse.cpp -o CMakeFiles/simd.dir/sse.cpp.s

embree/common/simd/CMakeFiles/simd.dir/sse.cpp.o.requires:

.PHONY : embree/common/simd/CMakeFiles/simd.dir/sse.cpp.o.requires

embree/common/simd/CMakeFiles/simd.dir/sse.cpp.o.provides: embree/common/simd/CMakeFiles/simd.dir/sse.cpp.o.requires
	$(MAKE) -f embree/common/simd/CMakeFiles/simd.dir/build.make embree/common/simd/CMakeFiles/simd.dir/sse.cpp.o.provides.build
.PHONY : embree/common/simd/CMakeFiles/simd.dir/sse.cpp.o.provides

embree/common/simd/CMakeFiles/simd.dir/sse.cpp.o.provides.build: embree/common/simd/CMakeFiles/simd.dir/sse.cpp.o


# Object files for target simd
simd_OBJECTS = \
"CMakeFiles/simd.dir/sse.cpp.o"

# External object files for target simd
simd_EXTERNAL_OBJECTS =

embree/libsimd.a: embree/common/simd/CMakeFiles/simd.dir/sse.cpp.o
embree/libsimd.a: embree/common/simd/CMakeFiles/simd.dir/build.make
embree/libsimd.a: embree/common/simd/CMakeFiles/simd.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/chris/surf/fracmap/libigl/tutorial/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX static library ../../libsimd.a"
	cd /home/chris/surf/fracmap/libigl/tutorial/build/embree/common/simd && $(CMAKE_COMMAND) -P CMakeFiles/simd.dir/cmake_clean_target.cmake
	cd /home/chris/surf/fracmap/libigl/tutorial/build/embree/common/simd && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/simd.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
embree/common/simd/CMakeFiles/simd.dir/build: embree/libsimd.a

.PHONY : embree/common/simd/CMakeFiles/simd.dir/build

embree/common/simd/CMakeFiles/simd.dir/requires: embree/common/simd/CMakeFiles/simd.dir/sse.cpp.o.requires

.PHONY : embree/common/simd/CMakeFiles/simd.dir/requires

embree/common/simd/CMakeFiles/simd.dir/clean:
	cd /home/chris/surf/fracmap/libigl/tutorial/build/embree/common/simd && $(CMAKE_COMMAND) -P CMakeFiles/simd.dir/cmake_clean.cmake
.PHONY : embree/common/simd/CMakeFiles/simd.dir/clean

embree/common/simd/CMakeFiles/simd.dir/depend:
	cd /home/chris/surf/fracmap/libigl/tutorial/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/chris/surf/fracmap/libigl/tutorial /home/chris/surf/fracmap/libigl/external/embree/common/simd /home/chris/surf/fracmap/libigl/tutorial/build /home/chris/surf/fracmap/libigl/tutorial/build/embree/common/simd /home/chris/surf/fracmap/libigl/tutorial/build/embree/common/simd/CMakeFiles/simd.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : embree/common/simd/CMakeFiles/simd.dir/depend

