#!/usr/bin/env gnuplot

set datafile separator ","
set terminal wxt
set grid
set xrange [0:1]
set yrange [0:1]
set size square
set title 'Kernel SVM : Sigma = 0.5, Lamnda = 1.0E-5'
plot   "data_class_A.csv"  using 1:2 with points pt 7 ps 2 lc '#FF3333' title 'Class A'
replot "data_class_A.csv"  using 1:2 with points pt 7 ps 2 lc '#3333FF' title 'Class B'
replot "data_bound_2d.csv" using 1:2 with lines       lw 2 lc '#666666' title 'Classification boundary'

pause -1

# vim: filetype=gnuplot
