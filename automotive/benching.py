#!/usr/bin/env python3
import os
from subprocess import PIPE, run
from glob import glob
import itertools
import sys
sys.path.append("./")
from compilation import *

def exe_small():
    rval = run(['./runme_small.sh'], stdout=PIPE, stderr=PIPE, text=True)
    return (rval.stdout, rval.stderr)

def exe_large():
    rval = run(['./runme_large.sh'], stdout=PIPE, stderr=PIPE, text=True)
    return (rval.stdout, rval.stderr)

def writeto(fp, data, title):
    fp.write(title)
    fp.write(data[0])
    fp.write(data[1])
    fp.write("###########"*5+"\n")
    
def exe_bench(dirname, cflags, outfile):
    os.chdir(dirname)
    prev = os.listdir(dirname)
    # comp = run(cflags, stdout=PIPE, stderr=PIPE)
    
    post = os.listdir(dirname)
    binexe = list(set(post) - set(prev))
    cwd = os.path.basename(os.getcwd())
    print("CWD: {}".format(cwd))
    with open(outfile, "a") as fp:
        if cwd == "qsort":
            t_small = exe_small()
            writeto(fp, t_small, cwd.upper()+" SMALL timings: \n"+" ".join(cflags))
            t_large = exe_large()
            writeto(fp, t_large, cwd.upper()+" LARGE timings: \n"+" ".join(cflags))
        elif cwd == "susan":
            t_small = exe_small()
            writeto(fp, t_small, cwd.upper()+" SMALL timings: \n"+" ".join(cflags))
            t_large = exe_large()
            writeto(fp, t_large, cwd.upper()+" LARGE timings: \n"+" ".join(cflags))
        elif cwd == "bitcount":
            t_small = exe_small()
            writeto(fp, t_small, cwd.upper()+" SMALL timings: \n"+" ".join(cflags))
            t_large = exe_large()
            writeto(fp, t_large, cwd.upper()+" LARGE timings: \n"+" ".join(cflags))
        elif cwd == "basicmath":
            t_small = exe_small()
            writeto(fp, t_small, cwd.upper()+" SMALL timings: \n"+" ".join(cflags))
            t_large = exe_large()
            writeto(fp, t_large, cwd.upper()+" LARGE timings: \n"+" ".join(cflags))

src_dir = "/home/russellb/DrEzhil/codebase/comp_eznew/automotive"
benchdirs = [os.path.join(src_dir, d) for d in os.listdir(src_dir) if os.path.isdir(os.path.join(src_dir, d))]

def exe_clean(dirname):
    os.chdir(dirname)
    cln = run(['make', 'clean'], stdout=PIPE, stderr=PIPE, shell=True)
    if cln.returncode == 0:
        return True
    else:
        return False

# Clean binaries before run
for d in benchdirs:
    if exe_clean(os.path.join(src_dir, d)):
        print("Successfully cleaned: {}".format(os.path.join(src_dir, d)))
    else:
        print("Not cleaned: {}".format(os.path.join(src_dir, d)))

ez_flags = ["-foptimize-register-move", "-ftree-loop-if-convert", "-fmerge-constants", "-ftree-coalesce-inlined-vars", "-fwhole-program"]

perm_list = [list(itertools.combinations(ez_flags, i)) for i in range(1,len(ez_flags)+1)]

outputfile="/home/russellb/DrEzhil/codebase/comp_eznew/automotive_output.txt"
# Execute compilation and run
for d in benchdirs:
    print("Starting to compile: {}\n".format(d))
    if exe_clean(os.path.join(src_dir, d)):
        print("Successfully cleaned: {}".format(os.path.join(src_dir, d)))
    else:
        print("Not cleaned: {}".format(os.path.join(src_dir, d)))
    for x in perm_list:
        cflags = list(x[0])
        compile_src(d, cflags, False)
        exe_bench(d, cflags, outputfile)
