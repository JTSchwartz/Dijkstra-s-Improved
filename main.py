from itertools import islice
import os
import sys
from vertex import *


def main():
	try:  # TODO: Dynamically read file
		with os.open(sys.argv[0]) as file:
			v_total, e_total = file.readline().split()

			for line in islice(file, 1, v_total + 2):
				split = line.split()
				Vertex(int(split[0]), int(split[1]), int(split[2]))

			for line in islice(file, v_total + 2, v_total + e_total + 2):
				edge = line.split()
				dist = Vertex.all_nodes[int(edge[0])].add_neighbor(int(edge[1]))
				Vertex.all_nodes[int(edge[1])].add_neighbor(int(edge[0]), dist)

			start, end = file.readlines()[-1].split()

	except IOError:
		print("File cannot be found")
		exit(1)

	# TODO: Verify this is useless
	# nodes = Vertex.all_nodes
	# for node in nodes:
	# 	if len(node.neighbors) == 2 and node.id is not start or node.id is not end:
	# 		x = node.neighbors[0]
	# 		y = node.neighbors[1]
	# 		dist = node.get_dist(x) + node.get_dist(y)
	# 		nodes.get(x).add_neighbor(y, dist)
	# 		nodes.get(y).add_neighbor(x, dist)
	# 		x.remove_neighbor(node)
	# 		y.remove_neighbor(node)


if __name__ == '__main__':
	main()
