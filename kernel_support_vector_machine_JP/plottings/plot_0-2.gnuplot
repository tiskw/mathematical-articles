#!/usr/bin/env gnuplot

set datafile separator ","
set terminal wxt
set grid
set xrange [0:1]
set yrange [0:1]
set size square
set title 'SVM'
plot   "data_class_A.csv" using 1:2 with points pt 7 ps 2 lc '#FF3333' title 'Class A'
replot "data_class_B.csv" using 1:2 with points pt 7 ps 2 lc '#3333FF' title 'Class B'
replot 0.9 - x                      with lines       lw 2 lc '#666666' title 'Classificatino boundary'

pause -1

# vim: filetype=gnuplot
