#!/usr/bin/env gnuplot

set datafile separator ","
set terminal svg size 1280, 320 font ",10"
set output 'kernel_approximation.svg'

set multiplot layout 1, 4

set title "RFF (dim=10)"
set grid
set xrange [0:100]
set yrange [0:100]
set zrange [0:1]
set cbrange [0:1]
set xtics ("-1.0" 0, "-0.5" 25, "0.0" 50, "0.5" 75, "1.0" 100)
set ytics ("-1.0" 0, "-0.5" 25, "0.0" 50, "0.5" 75, "1.0" 100)
set size square
unset key
plot "data_rff_1e1.csv" using 1:2:3 with image

set title "RFF (dim=100)"
set grid
set xrange [0:100]
set yrange [0:100]
set zrange [0:1]
set cbrange [0:1]
set xtics ("-1.0" 0, "-0.5" 25, "0.0" 50, "0.5" 75, "1.0" 100)
set ytics ("-1.0" 0, "-0.5" 25, "0.0" 50, "0.5" 75, "1.0" 100)
set size square
unset key
plot "data_rff_1e2.csv" using 1:2:3 with image

set title "RFF (dim=1000)"
set grid
set xrange [0:100]
set yrange [0:100]
set zrange [0:1]
set cbrange [0:1]
set xtics ("-1.0" 0, "-0.5" 25, "0.0" 50, "0.5" 75, "1.0" 100)
set ytics ("-1.0" 0, "-0.5" 25, "0.0" 50, "0.5" 75, "1.0" 100)
set size square
unset key
plot "data_rff_1e3.csv" using 1:2:3 with image

set title "RBF kernel"
set grid
set xrange [0:100]
set yrange [0:100]
set zrange [0:1]
set cbrange [0:1]
set xtics ("-1.0" 0, "-0.5" 25, "0.0" 50, "0.5" 75, "1.0" 100)
set ytics ("-1.0" 0, "-0.5" 25, "0.0" 50, "0.5" 75, "1.0" 100)
set size square
unset key
plot "data_kernel.csv" using 1:2:3 with image

# vim: filetype=gnuplot
