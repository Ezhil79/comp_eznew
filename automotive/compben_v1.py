#!/usr/bin/env python3

import os
from subprocess import PIPE, run

def exe():
    rval = run(['./runme_small.sh'], stdout=PIPE, stderr=PIPE, text=True)
    rval1 = run(['./runme_large.sh'], stdout=PIPE, stderr=PIPE, text=True)
    return (rval.stdout, rval.stderr, rval1.stdout, rval1.stderr)

def writeto(fp, data, title):
    fp.write(title)
    fp.write(data[0])
    fp.write(data[1])
    fp.write(data[2])
    fp.write(data[3])
    fp.write("###########"*5+"\n")

    
def exe_bench(dirname, cflags, outfile):
    os.chdir(dirname)
    cln = run(['make', 'clean'], stdout=PIPE, stderr=PIPE)
    prev = os.listdir(dirname)
    comp = run(cflags, stdout=PIPE, stderr=PIPE)

    
    post = os.listdir(dirname)
    binexe = list(set(post) - set(prev))
    cwd = os.path.basename(os.getcwd())
    with open(outfile, "a") as fp:
        if cwd == "qsort":
            t = exe()
            writeto(fp, t, cwd.upper()+" timings: \n")
        elif cwd == "susan":
            t = exe()
            writeto(fp, t, cwd.upper()+" timings: \n")
        elif cwd == "bitcount":
            t = exe()
            writeto(fp, t, cwd.upper()+" timings: \n")
        elif cwd == "basicmath":
            t = exe()
            writeto(fp, t, cwd.upper()+" timings: \n")
                

#src_dir = input("Enter the location of mibench - automotive benchmark directory: ")
src_dir = "/home/russellb/DrEzhil/benchmark_inputs/automotive"
benchdirs = [os.path.join(src_dir, d) for d in os.listdir(src_dir) if os.path.isdir(os.path.join(src_dir, d))]

mycflags = ['make']
print("Automotive only")
ofile = src_dir+"/automotive.txt"
if os.path.isfile(ofile):
    os.remove(ofile)
else:
    ofile

for d in benchdirs:
    exe_bench(os.path.join(src_dir, d), mycflags[0], ofile)
