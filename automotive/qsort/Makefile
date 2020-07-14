FILE1 = qsort_small.c
FILE2 = qsort_large.c

all: qsort_small qsort_large

qsort_small: qsort_small.c Makefile
	gcc -static qsort_small.c -O3 -o qsort_small -lm
qsort_large: qsort_large.c Makefile
	gcc -static qsort_large.c -O3 -o qsort_large -lm

clean:
	rm -rf qsort_small qsort_small1 qsort_small2 qsort_small3 qsort_small4 qsort_small5 qsort_large qsort_large1 qsort_large2 qsort_large3 qsort_large4 qsort_large5 output*
