#!/usr/bin/env python3
import os
from subprocess import PIPE, run
from glob import glob
import itertools

def compile_src(dirname, cflags):
    os.chdir(dirname)
    pwd = os.getcwd()
    cwd = os.path.basename(pwd)
    if cwd == "qsort":
        static_flags = ["gcc", "-static", "-O3", "-lm", "qsort_small.c", "-o", "qsort_small"+str(len(cflags)), "-funroll-all-loops", "-fno-tree-loop-optimize", "-fno-inline-functions", "-funsafe-math-optimizations", "-fno-guess-branch-probability", "-fno-ivopts", "-frecord-gcc-switches"]
        full_flags = static_flags + cflags
        comp = run(full_flags, stdout=PIPE, stderr=PIPE)
        if comp.returncode == 0:
            print("Compilation of: \n{}\n is successfull!!".format(" ".join(full_flags)))
        else:
            print("Compilation failed with: \n{}\n".format(comp.stderr))
            
        static_flags1 = ["gcc", "-static", "-O3", "-lm", "qsort_large.c", "-o", "qsort_large"+str(len(cflags)), "-funroll-all-loops", "-fno-tree-loop-optimize", "-fno-inline-functions", "-funsafe-math-optimizations", "-fno-guess-branch-probability", "-fno-ivopts", "-frecord-gcc-switches"]
        full_flags1 = static_flags1 + cflags
        comp1 = run(full_flags1, stdout=PIPE, stderr=PIPE)
        if comp1.returncode == 0:
            print("Compilation of: \n{}\n is successfull!!".format(" ".join(full_flags1)))
        else:
            print("Compilation failed with: \n{}\n".format(comp1.stderr))
    elif cwd == "susan":
        static_flags = ["gcc", "-static", "-O4", "susan.c", "-o", "susan"+str(len(cflags)), "-lm", "-funroll-all-loops", "-fno-tree-loop-optimize", "-fno-inline-functions", "-funsafe-math-optimizations", "-fno-guess-branch-probability", "-fno-ivopts", "-frecord-gcc-switches"]
        full_flags = static_flags + cflags
        comp = run(full_flags, stdout=PIPE, stderr=PIPE)
        if comp.returncode == 0:
            print("Compilation of: \n{}\n is successfull!!".format(" ".join(full_flags)))
        else:
            print("Compilation failed with: \n{}\n".format(comp.stderr))
    elif cwd == "bitcount":
        static_flags = ["gcc", "-static", "-O3", "bitcnt_1.c", "bitcnt_2.c", "bitcnt_3.c", "bitcnt_4.c", "bitfiles.c", "bitstrng.c", "bstr_i.c", "bitcnts.c", "-funroll-all-loops", "-fno-tree-loop-optimize", "-fno-inline-functions", "-funsafe-math-optimizations", "-fno-guess-branch-probability", "-fno-ivopts", "-o", "bitcounts"+str(len(cflags)), "-frecord-gcc-switches"]
        full_flags = static_flags + cflags
        comp = run(full_flags, stdout=PIPE, stderr=PIPE)
        if comp.returncode == 0:
            print("Compilation of: \n{}\n is successfull!!".format(" ".join(full_flags)))
        else:
            print("Compilation failed with: \n{}\n".format(comp.stderr))
    elif cwd == "basicmath":
        static_flags = ["gcc", "-static", "-O3", "basicmath_small.c", "rad2deg.c", "cubic.c", "isqrt.c", "-o", "basicmath_small"+str(len(cflags)), "-lm", "-funroll-all-loops", "-fno-tree-loop-optimize", "-fno-inline-functions", "-funsafe-math-optimizations", "-fno-guess-branch-probability", "-fno-ivopts", "-frecord-gcc-switches"]
        full_flags = static_flags + cflags
        comp = run(full_flags, stdout=PIPE, stderr=PIPE)
        if comp.returncode == 0:
            print("Compilation of: \n{}\n is successfull!!".format(" ".join(full_flags)))
        else:
            print("Compilation failed with: \n{}\n".format(comp.stderr))
        static_flags1 = ["gcc", "-static", "-O3", "basicmath_large.c", "rad2deg.c", "cubic.c", "isqrt.c", "-o", "basicmath_large"+str(len(cflags)), "-lm", "-funroll-all-loops", "-fno-tree-loop-optimize", "-fno-inline-functions", "-funsafe-math-optimizations", "-fno-guess-branch-probability", "-fno-ivopts", "-frecord-gcc-switches"]
        full_flags1 = static_flags1 + cflags
        comp1 = run(full_flags1, stdout=PIPE, stderr=PIPE)
        if comp1.returncode == 0:
            print("Compilation of: \n{}\n is successfull!!".format(" ".join(full_flags1)))
        else:
            print("Compilation failed with: \n{}\n".format(comp1.stderr))

        
src_dir = "/home/russellb/DrEzhil/codebase/comp_eznew/automotive"
benchdirs = [os.path.join(src_dir, d) for d in os.listdir(src_dir) if os.path.isdir(os.path.join(src_dir, d))]

def exe_clean(dirname):
    os.chdir(dirname)
    cln = run(['make', 'clean'], stdout=PIPE, stderr=PIPE)
    if cln.returncode == 0:
        return True
    else:
        return False

ofile = src_dir+"/automotive.txt"

if os.path.isfile(ofile):
    os.remove(ofile)
else:
    ofile

# Clean binaries before run
for d in benchdirs:
    if exe_clean(os.path.join(src_dir, d)):
        print("Successfully cleaned: {}".format(os.path.join(src_dir, d)))
    else:
        print("Not cleaned: {}".format(os.path.join(src_dir, d)))

ez_flags = ["-foptimize-register-move", "-ftree-loop-if-convert", "-fmerge-constants", "-ftree-coalesce-inlined-vars", "-fwhole-program"]

perm_list = [list(itertools.combinations(ez_flags, i)) for i in range(1,len(ez_flags)+1)]

for x in perm_list:
    print(list(x[0]))

# Execute compilation and run
for d in benchdirs:
    for x in perm_list:
        compile_src(d, list(x[0]))
