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
plot 'lines_of_code_by_author.dat' using 1:2 title "Jack Nagel" w lines, 'lines_of_code_by_author.dat' using 1:3 title "Adam Vandenberg" w lines, 'lines_of_code_by_author.dat' using 1:4 title "BrewTestBot" w lines, 'lines_of_code_by_author.dat' using 1:5 title "Mike McQuaid" w lines, 'lines_of_code_by_author.dat' using 1:6 title "Brett Koonce" w lines, 'lines_of_code_by_author.dat' using 1:7 title "Max Howell" w lines, 'lines_of_code_by_author.dat' using 1:8 title "Misty De Meo" w lines, 'lines_of_code_by_author.dat' using 1:9 title "Charlie Sharpsteen" w lines, 'lines_of_code_by_author.dat' using 1:10 title "Dominyk Tiller" w lines, 'lines_of_code_by_author.dat' using 1:11 title "nibbles 2bits" w lines, 'lines_of_code_by_author.dat' using 1:12 title "David Höppner" w lines, 'lines_of_code_by_author.dat' using 1:13 title "Samuel John" w lines, 'lines_of_code_by_author.dat' using 1:14 title "Alexis Hildebrandt" w lines, 'lines_of_code_by_author.dat' using 1:15 title "Xu Cheng" w lines, 'lines_of_code_by_author.dat' using 1:16 title "Baptiste Fontaine" w lines, 'lines_of_code_by_author.dat' using 1:17 title "Stefan" w lines, 'lines_of_code_by_author.dat' using 1:18 title "Tim D. Smith" w lines, 'lines_of_code_by_author.dat' using 1:19 title "Xiyue Deng" w lines, 'lines_of_code_by_author.dat' using 1:20 title "Mike Naberezny" w lines, 'lines_of_code_by_author.dat' using 1:21 title "David Christenson" w lines
