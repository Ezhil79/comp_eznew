#!/bin/sh
echo "susan small -smoothing"
time ./susan input_small.pgm output_small.smoothing.pgm -s > susan_small_smooth.txt

echo "susan small -edges"
time ./susan input_small.pgm output_small.edges.pgm -e > susan_small_edges.txt

echo "susan small -corners"
time ./susan input_small.pgm output_small.corners.pgm -c > susan_small_corners.txt

