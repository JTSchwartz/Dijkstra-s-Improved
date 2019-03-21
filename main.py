from heapq import *
from itertools import islice
from math import log
from random import randrange
import sys
from vertex import *


def main():
	start_end, v_total, e_total = [], 0, 0

	try:
		with open(sys.argv[1]) as file:
			ve_totals = file.readline().split()
			v_total, e_total = int(ve_totals[0]), int(ve_totals[1])

			# Read in all listed Vertices
			print("Vertices:", v_total)
			for line in islice(file, 0, v_total):
				split = line.split()
				Vertex(int(split[0]), int(split[1]), int(split[2]))

			# Read in all Nodes
			print("Edges:", e_total)
			for line in islice(file, 0, e_total):
				edge = line.split()
				dist = Vertex.all_nodes[int(edge[0])].add_neighbor(int(edge[1]))  # Return distance so it wont be calculated again
				Vertex.all_nodes[int(edge[1])].add_neighbor(int(edge[0]), dist)

			start_end = file.readline().split()  # Last line may hold a provided start and end node
			print("Finished reading in file")

	except IOError:
		print("File not found")
		exit(1)

	if len(start_end) == 0:  # Not all inputs will specify a start and end node
		# Choose two numbers within N
		start = Vertex.all_nodes[randrange(v_total)]
		end = Vertex.all_nodes[randrange(v_total)]

		while end == start:  # Ensure that Start and End are not the same node
			end = Vertex.all_nodes[randrange(v_total)]

	else:  # Handles inputs that provide a start and end
		start = Vertex.all_nodes[int(start_end[0])]
		end = Vertex.all_nodes[int(start_end[1])]

	print("Start:", start.id, "End:", end.id)

	v_count = e_count = start.dist = 0  # Initiate counts as 0 and set the distance of the start node as 0
	queue = []  # List that will be used as a priority queue for Dijkstra's
	heappush(queue, start)

	while len(queue) != 0:
		cur = heappop(queue)
		v_count += 1

		if cur is end:
			continue
		elif end in cur.neighbors:  # A straight line is always shortest, other neighbors cannot have shorter paths
			if end.dist > cur.dist + cur.get_dist(end.id):
				e_count += 1
				end.parent = cur.id
				end.dist = cur.dist + cur.get_dist(end.id)

			if end.dist <= e_log_v(e_count, v_count):  # E' Log V' is theoretically the shortest possible distance to a node
				break

			continue

		# Test all of the current nodes neighbors to see if this node can offer a shorter distance
		for adj_id in cur.neighbors:
			adj = Vertex.all_nodes[adj_id]
			proposed_dist = cur.dist + cur.get_dist(adj.id)
			e_count += 1

			if adj.dist > proposed_dist:
				adj.dist = proposed_dist
				adj.parent = cur.id
				heappush(queue, adj)

	# Reverse engineer the shortest distance and append to list to be read in proper order
	hop, path = end, []
	while hop is not start:
		path.append(hop)
		hop = Vertex.all_nodes[hop.parent]

	print("Path:", start.id, "Distance:", 0)

	while len(path) != 0:
		node = path.pop()
		print("Path: {0:d} Distance: {1:.2f}".format(node.id, node.dist))


# Simplified call for assumed shortest distance
def e_log_v(e, v):
	return e * log(v)


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("Usage: dijkstra.exe [input file]")

	main()
