#!/usr/bin/env python3
import os
from subprocess import PIPE, run
from glob import glob
import itertools
import sys
sys.path.append("./")
from compilation import *

import csv

def exe_small():
    rval = run(['./runme_small.sh'], stdout=PIPE, stderr=PIPE, text=True)
    return (rval.stdout, rval.stderr)

def exe_large():
    rval = run(['./runme_large.sh'], stdout=PIPE, stderr=PIPE, text=True)
    return (rval.stdout, rval.stderr)

def writeto(fp, data, title):
    print(data)
    fp.writerow([title])
    subhead = [s.strip().split('\n') for s in data[0].splitlines()]
    for sh in subhead:
        fp.writerow(sh)
    # fp.writerow(data[0].split('\n'))
    tim = [s.strip().split('\t') for s in data[1].splitlines()]
    for t in tim:
        fp.writerow(t)
    fp.writerow(["###########"*5+"\n"])
    
def exe_bench(dirname, cflags, outfile):
    os.chdir(dirname)
    prev = os.listdir(dirname)
    
    post = os.listdir(dirname)
    binexe = list(set(post) - set(prev))
    cwd = os.path.basename(os.getcwd())
    print("CWD: {}".format(cwd))
    with open(outfile, "a") as fp:
        outwrite = csv.writer(fp, delimiter=",",  quoting=csv.QUOTE_NONNUMERIC)
        if cwd == "qsort":
            t_small = exe_small()
            writeto(outwrite, t_small, cwd.upper()+" SMALL timings: \n"+" ".join(cflags))
            t_large = exe_large()
            writeto(outwrite, t_large, cwd.upper()+" LARGE timings: \n"+" ".join(cflags))
        elif cwd == "susan":
            t_small = exe_small()
            writeto(outwrite, t_small, cwd.upper()+" SMALL timings: \n"+" ".join(cflags))
            t_large = exe_large()
            writeto(outwrite, t_large, cwd.upper()+" LARGE timings: \n"+" ".join(cflags))
        elif cwd == "bitcount":
            t_small = exe_small()
            writeto(outwrite, t_small, cwd.upper()+" SMALL timings: \n"+" ".join(cflags))
            t_large = exe_large()
            writeto(outwrite, t_large, cwd.upper()+" LARGE timings: \n"+" ".join(cflags))
        elif cwd == "basicmath":
            t_small = exe_small()
            writeto(outwrite, t_small, cwd.upper()+" SMALL timings: \n"+" ".join(cflags))
            t_large = exe_large()
            writeto(outwrite, t_large, cwd.upper()+" LARGE timings: \n"+" ".join(cflags))

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

ez_flags = ["", "-foptimize-register-move", "-ftree-loop-if-convert"]

perm_list = [list(itertools.combinations(ez_flags, i)) for i in range(1,len(ez_flags)+1)]

outputfile="/home/russellb/DrEzhil/codebase/comp_eznew/output.csv"
# Execute compilation and run
for d in benchdirs:
    print("Starting to compile: {}\n".format(d))
    if exe_clean(os.path.join(src_dir, d)):
        print("Successfully cleaned: {}".format(os.path.join(src_dir, d)))
    else:
        print("Not cleaned: {}".format(os.path.join(src_dir, d)))
    for x in perm_list:
        print("Num flags: {}".format(len(x)))
        for ix in x:
            cflags = list(ix)
            compile_src(d, cflags, False)
            exe_bench(d, cflags, outputfile)
