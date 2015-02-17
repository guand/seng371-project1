set terminal png transparent size 640,240
set size 1.0,1.0

set terminal png transparent size 640,480
set output 'commits_by_author.png'
set key left top
set yrange [0:]
set xdata time
set timefmt "%s"
set format x "%Y-%m-%d"
set grid y
set ylabel "Commits"
set xtics rotate
set bmargin 6
plot 'commits_by_author.dat' using 1:2 title "Jeremy Ashkenas" w lines, 'commits_by_author.dat' using 1:3 title "Brad Dunbar" w lines, 'commits_by_author.dat' using 1:4 title "Adam Krebs" w lines, 'commits_by_author.dat' using 1:5 title "Casey Foster" w lines, 'commits_by_author.dat' using 1:6 title "Tim Griesser" w lines, 'commits_by_author.dat' using 1:7 title "brad dunbar" w lines, 'commits_by_author.dat' using 1:8 title "Jimmy Yuen Ho Wong" w lines, 'commits_by_author.dat' using 1:9 title "Sam Breed" w lines, 'commits_by_author.dat' using 1:10 title "Justin Ridgewell" w lines, 'commits_by_author.dat' using 1:11 title "Genadi Samokovarov" w lines, 'commits_by_author.dat' using 1:12 title "Samuel Clay" w lines, 'commits_by_author.dat' using 1:13 title "Phil Freo" w lines, 'commits_by_author.dat' using 1:14 title "Tim Branyen" w lines, 'commits_by_author.dat' using 1:15 title "Jeff Larson" w lines, 'commits_by_author.dat' using 1:16 title "KungD" w lines, 'commits_by_author.dat' using 1:17 title "Irene Ros" w lines, 'commits_by_author.dat' using 1:18 title "Ted Han" w lines, 'commits_by_author.dat' using 1:19 title "Paul Uithol" w lines, 'commits_by_author.dat' using 1:20 title "Matt Smith" w lines, 'commits_by_author.dat' using 1:21 title "Harry Wolff" w lines
