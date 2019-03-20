from heapq import *
from itertools import islice
from math import log
import sys
from vertex import *


def main():
	start_end = []

	try:  # TODO: Dynamically read file
		with open(sys.argv[1]) as file:
			ve_counts = file.readline().split()
			v_total, e_total = int(ve_counts[0]), int(ve_counts[1])

			for line in islice(file, 0, v_total):
				split = line.split()
				Vertex(int(split[0]), int(split[1]), int(split[2]))

			for line in islice(file, 0, e_total):
				edge = line.split()
				dist = Vertex.all_nodes[int(edge[0])].add_neighbor(int(edge[1]))
				Vertex.all_nodes[int(edge[1])].add_neighbor(int(edge[0]), dist)
				# print(line)

			start_end = file.readline().split()

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

	queue = []
	start = Vertex.all_nodes[int(start_end[0])]
	end = Vertex.all_nodes[int(start_end[1])]
	v_count = e_count = start.dist = 0
	heappush(queue, start)

	while True:
		if len(queue) == 0:
			# print("Broke")
			break

		cur = heappop(queue)
		# print("Cur:", cur.id)
		v_count += 1

		if cur is end:
			continue
		elif end in cur.neighbors:  # A straight line is always shortest, other neighbors cannot have shorter paths
			if end.dist > cur.dist + cur.get_dist(end.id):
				e_count += 1
				end.parent = cur.id
				end.dist = cur.dist + cur.get_dist(end.id)

			if end.dist <= e_log_v(e_count, v_count):
				# print("ELogV")
				break

			continue

		for adj_id in cur.neighbors:
			adj = Vertex.all_nodes[adj_id]
			this_dist = cur.dist + cur.get_dist(adj.id)
			# print(cur.id, "to", adj.id, ":", this_dist)
			e_count += 1

			if adj.dist > this_dist:
				adj.dist = this_dist
				adj.parent = cur.id
				heappush(queue, adj)

	hop = end
	path = []
	while hop is not start:
		path.append(hop)
		hop = Vertex.all_nodes[hop.parent]

	print("Path:", start.id, "Distance:", 0)

	while len(path) != 0:
		node = path.pop()
		print("Path: {0:d} Distance: {1:.2f}".format(node.id, node.dist))


def e_log_v(e, v):
	return e * log(v)


if __name__ == '__main__':
	main()
