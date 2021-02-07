#!/usr/bin/env gnuplot

$data1 << EOD
-1 0
1 0
1 1
2 1
EOD

$data2 << EOD
-1 0
0 0
2 2
EOD

set grid
set xrange [-1:2]
set yrange [-0.5:2.5]
unset key

set terminal wxt 1
plot   $data1 with lines lw 2 lc '#FF3333'
replot x**2   with lines lw 2 lc '#3333FF'

set terminal wxt 2
plot   $data1 with lines lw 2 lc '#FF3333'
replot $data2 with lines lw 2 lc '#33FF33'

pause -1

# vim: filetype=gnuplot
