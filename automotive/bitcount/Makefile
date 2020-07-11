FILE = bitcount_1.c bitcount_2.c bitcount_3.c bitcount_4.c bitcounts.c bitfiles.c bitstrng.c bstr_i.c 

bitcounts: ${FILE} Makefile
	gcc -static ${FILE} -O3 -o bitcounts

clean:
	rm -rf bitcounts output*
