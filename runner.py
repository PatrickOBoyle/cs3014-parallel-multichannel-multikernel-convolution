from subprocess import call

call(["gcc", "-O3", "-fopenmp", "-msse4", "conv-harness.c"])
call(["echo", "GCC finished"])

call(["echo", "Running 100x100 tests..."])
call(["./a.out", "100", "100", "1", "1", "1"])
call(["./a.out", "100", "100", "1", "3", "3"])
call(["./a.out", "100", "100", "3", "3", "3"])
call(["./a.out", "100", "100", "3", "10", "10"])

call(["echo", "Running 500x500 tests..."])
call(["./a.out", "500", "500", "3", "10", "10"])

call(["echo", "Running 1000x1000 tests..."])
call(["./a.out", "1000", "1000", "3", "10", "10"])

call(["echo", "Running 2000x2000 tests..."])
call(["./a.out", "2000", "2000", "3", "10", "10"])

call(["echo", "Running 3000x3000 tests..."])
call(["./a.out", "3000", "3000", "3", "10", "10"])
