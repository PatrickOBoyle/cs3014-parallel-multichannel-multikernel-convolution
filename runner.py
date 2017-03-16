from subprocess import call

call(["gcc", "-O3", "-fopenmp", "-msse4", "conv-harness.c"])
call(["./a.out", "2000", "2000", "3", "10", "10"])
