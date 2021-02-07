#!/usr/bin/env gnuplot

set datafile separator ","
set terminal wxt
set palette defined (\
    0 '#000090', 1 '#000fff', 2 '#0090ff',\
    3 '#0fffee', 4 '#90ff70', 5 '#ffee00',\
    6 '#ff7000', 7 '#ee0000', 8 '#7f0000')
set grid
set xrange [0:1]
set yrange [0:1]
set title 'Sigma = 0.03, Lambda = 1.0E-5'
unset colorbox
splot  "data_class_A.csv"        using 1:2:3 with points pt 7 ps 2 lc '#FF3333' title 'class A'
replot "data_class_B.csv"        using 1:2:3 with points pt 7 ps 2 lc '#3333FF' title 'class B'
replot "data_reg_3d_overfit.csv" using 1:2:3 with lines lw 2 palette            title 'Regression curve'

pause -1

# vim: filetype=gnuplot
