#!/usr/bin/env python3

import os
from subprocess import PIPE, run
from glob import glob

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

# def compile_src(dirname):
#     cwd = os.chdir(dirname)
#     print("COMPILE DIR: {}".format(cwd))
#     if cwd == "qsort":
#         static_flags = ["gcc", "-static", "-O3", "-lm", "qsort_small.c", "-o", "qsort_small"]
#         full_flags = static_flags
#         comp = run(full_flags, stdout=PIPE, stderr=PIPE)
#     elif cwd == "susan":
#         static_flags = ["gcc", "-static", "-O4", "-lm", "susan.c", "-o", "susan"]
#         full_flags = static_flags
#         comp = run(full_flags, stdout=PIPE, stderr=PIPE)
#     elif cwd == "bitcount":
#         static_flags = ["gcc", "-static", "-O3", "bitcnt_1.c", "bitcnt_2.c", "bitcnt_3.c", "bitcnt_4.c", "bitfiles.c", "bitstring.c", "bstr_i.c", "bitcnts.c"]
#         full_flags = static_flags
#         comp = run(full_flags, stdout=PIPE, stderr=PIPE)
#     elif cwd == "basicmath":
#         static_flags = ["gcc", "-static", "-O3", "-lm", "basicmath_small.c", "rad2deg.c", "cubic.c", "isqrt.c", "-o", "basicmath_small"]
#         full_flags = static_flags
#         comp = run(full_flags, stdout=PIPE, stderr=PIPE)
    
def exe_bench(dirname, cflags, outfile):
    os.chdir(dirname)
    prev = os.listdir(dirname)
    comp = run(cflags, stdout=PIPE, stderr=PIPE)
    
    post = os.listdir(dirname)
    binexe = list(set(post) - set(prev))
    cwd = os.path.basename(os.getcwd())
    print("CWD: {}".format(cwd))
    with open(outfile, "a") as fp:
        if cwd == "qsort":
            t_small = exe_small()
            writeto(fp, t_small, cwd.upper()+" timings: \n")
            t_large = exe_large()
            writeto(fp, t_large, cwd.upper()+" timings: \n")
        elif cwd == "susan":
            t_small = exe_small()
            writeto(fp, t_small, cwd.upper()+" timings: \n")
            t_large = exe_large()
            writeto(fp, t_large, cwd.upper()+" timings: \n")
        elif cwd == "bitcount":
            t_small = exe_small()
            writeto(fp, t_small, cwd.upper()+" timings: \n")
            t_large = exe_large()
            writeto(fp, t_large, cwd.upper()+" timings: \n")
        elif cwd == "basicmath":
            t_small = exe_small()
            writeto(fp, t_small, cwd.upper()+" timings: \n")
            t_large = exe_large()
            writeto(fp, t_large, cwd.upper()+" timings: \n")

def compile_src(dirname):
    cwd = os.path.basename(dirname)
    print("COMPILE DIR: {}".format(cwd))

    if cwd == "qsort":
        static_flags = ["gcc", "-static", "-O3", "-lm", "qsort_small.c", "-o", "qsort_small"]
        full_flags = static_flags
        comp = run(full_flags, stdout=PIPE, stderr=PIPE)
    elif cwd == "susan":
        static_flags = ["gcc", "-static", "-O4", "-lm", "susan.c", "-o", "susan"]
        full_flags = static_flags
        comp = run(full_flags, stdout=PIPE, stderr=PIPE)
    elif cwd == "bitcount":
        static_flags = ["gcc", "-static", "-O3", "bitcnt_1.c", "bitcnt_2.c", "bitcnt_3.c", "bitcnt_4.c", "bitfiles.c", "bitstring.c", "bstr_i.c", "bitcnts.c"]
        full_flags = static_flags
        comp = run(full_flags, stdout=PIPE, stderr=PIPE)
    elif cwd == "basicmath":
        static_flags = ["gcc", "-static", "-O3", "-lm", "basicmath_small.c", "rad2deg.c", "cubic.c", "isqrt.c", "-o", "basicmath_small"]
        full_flags = static_flags
        comp = run(full_flags, stdout=PIPE, stderr=PIPE)
        
#src_dir = input("Enter the location of mibench - automotive benchmark directory: ")
src_dir = "/home/russellb/DrEzhil/codebase/comp_eznew/automotive"
benchdirs = [os.path.join(src_dir, d) for d in os.listdir(src_dir) if os.path.isdir(os.path.join(src_dir, d))]

def exe_clean(dirname):
    os.chdir(dirname)
    cln = run(['make', 'clean'], stdout=PIPE, stderr=PIPE, shell=True)
    if cln.returncode == 0:
        return True
    else:
        return False

def get_src_file(dirnam):
    src_files = glob(os.path.join(dirnam,"*.c"))
    tmp = [os.path.basename(fl) for fl in src_files]
    return [i for i in tmp if os.path.basename(dirnam) in i]

def optflags(dirname):
    compiler = ['gcc', '-static']
    srcfile = get_src_file(dirname)
    oflags = ['-O3']
    lflags = ['-lm']
    opromp = ["-o"]
    binfil = [(src).rsplit(".",1)[0] for src in srcfile]
    bfile = [i for i in binfil if os.path.basename(dirname) in i]

    tmp = list()
    for x in range(len(bfile)):
        tmp.append(compiler+[srcfile[x]]+opromp+[bfile[x]]+oflags+lflags)
    return tmp

# print("Automotive only")
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

# Execute compilation and run
for d in benchdirs:
    print("DIR: {}".format(d))
    compile_src(d)
    # ss = optflags(os.path.join(src_dir, d))
    # print("SS: {}".format(ss))
    # if len(ss) > 1:
    # for s in ss:
    #     print("input for compile src: {}".format(os.path.join(src_dir, d)))
    #     compile_src(os.path.join(src_dir, d))
    #     exe_bench(os.path.join(src_dir, d), s, ofile)
    # else:
    #     exe_bench(os.path.join(src_dir, d), s, ofile)
