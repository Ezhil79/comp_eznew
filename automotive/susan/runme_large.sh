#!/bin/sh
echo "susan large - smooth"
time ./susan input_large.pgm output_large.smoothing.pgm -s > susan_small_smooth.txt

echo "susan large - edges"
time ./susan input_large.pgm output_large.edges.pgm -e > susan_large_edge.txt

echo "susan large - corners"
time ./susan input_large.pgm output_large.corners.pgm -c > susan_large_corner.txt

