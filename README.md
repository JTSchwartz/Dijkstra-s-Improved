Dijkstra's Algorithm Improved
---

Class: CPS 450

This program preforms Dijkstra's algorithm on a graph of nodes on an XY-coordinate plane.

It has improved on the original algorithm in 3 ways:
1. Distances between connected nodes are preprocessed
2. Stops if the current shortest path is equal or less than E' Log V' (Where E' and V' are the number of edges and vertices already examined)
3. If a node neighbors the end node, it will only test against the end node and none others, because a straight line is the shortest possible distance between 2 points

The input file (.txt) is read in through a command line argument and must be formatted as specified below:
* First line: [Vertices Count] [Edge Count] ex. `8 23`
* The next V lines are nodes and XY-coordinates numbered 0 to V - 1: [Node ID] [X Coord] [Y Coord] ex. `0 3 14`
* The next E lines are node neighbors (bidirectional): [Node A] [Node B] ex. `0 1`
* The last line is optional for explicitly declaring the start and end node, written just like neighbor lines
* There may be no blank lines

Example:\
6 9\
0  1000 2400\
1  2800 3000\
2  2400 2500\
3  4000    0\
4  4500 3800\
5  6000 1500\
0 1\
0 3\
1 2\
1 4\
2 4\
2 3\
2 5\
3 5\
4 5\
0 5