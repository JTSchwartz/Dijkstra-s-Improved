from itertools import islice
import os
import sys
from vertex import *


def main():
	try:
		with os.open(sys.argv[0]) as file:
			v_total, e_total = " ".split(file.readline())
			vertices = [] * v_total

			for line in islice(file, 1, v_total + 2):
				split = " ".split(line)
				vertices[int(split[0]) - 1] = Vertex(int(split[1]), int(split[2]))

			for line in islice(file, v_total + 2, v_total + e_total + 2):
				edge = " ".split(line)
				dist = vertices[int(edge[0])].add_neighbor(int(edge[1]))
				vertices[int(edge[1])].add_neighbor(int(edge[0]), dist)

			start, end = " ".split(file.readlines()[-1])

	except IOError:
		print("File cannot be found")
		exit(1)

	nodes = Vertex.all_nodes


if __name__ == '__main__':
	main()
