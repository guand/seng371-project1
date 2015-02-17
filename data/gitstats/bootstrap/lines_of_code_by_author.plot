set terminal png transparent size 640,240
set size 1.0,1.0

set terminal png transparent size 640,480
set output 'lines_of_code_by_author.png'
set key left top
set yrange [0:]
set xdata time
set timefmt "%s"
set format x "%Y-%m-%d"
set grid y
set ylabel "Lines"
set xtics rotate
set bmargin 6
plot 'lines_of_code_by_author.dat' using 1:2 title "Mark Otto" w lines, 'lines_of_code_by_author.dat' using 1:3 title "Chris Rebert" w lines, 'lines_of_code_by_author.dat' using 1:4 title "Jacob Thornton" w lines, 'lines_of_code_by_author.dat' using 1:5 title "XhmikosR" w lines, 'lines_of_code_by_author.dat' using 1:6 title "fat" w lines, 'lines_of_code_by_author.dat' using 1:7 title "Heinrich Fenkart" w lines, 'lines_of_code_by_author.dat' using 1:8 title "Zlatan Vasović" w lines, 'lines_of_code_by_author.dat' using 1:9 title "Julian Thilo" w lines, 'lines_of_code_by_author.dat' using 1:10 title "Patrick H. Lauke" w lines, 'lines_of_code_by_author.dat' using 1:11 title "Jacob" w lines, 'lines_of_code_by_author.dat' using 1:12 title "Robert Burns" w lines, 'lines_of_code_by_author.dat' using 1:13 title "Bootstrap's Grunt bot" w lines, 'lines_of_code_by_author.dat' using 1:14 title "Quy Ton" w lines, 'lines_of_code_by_author.dat' using 1:15 title "Pete Hopkins" w lines, 'lines_of_code_by_author.dat' using 1:16 title "Erik van der Kolk" w lines, 'lines_of_code_by_author.dat' using 1:17 title "Bas Bosman" w lines, 'lines_of_code_by_author.dat' using 1:18 title "vsn4ik" w lines, 'lines_of_code_by_author.dat' using 1:19 title "Steven Black" w lines, 'lines_of_code_by_author.dat' using 1:20 title "liuyl" w lines, 'lines_of_code_by_author.dat' using 1:21 title "Yohn" w lines
