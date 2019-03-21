from math import sqrt, inf


class Vertex:
	all_nodes = dict()  # Stores all nodes to find by ID

	# Each Node stores it's own coordinates, distance from starting node, and neighbors
	def __init__(self, id_num, x, y):
		Vertex.all_nodes[id_num] = self
		self.id = id_num
		self.x = x
		self.y = y
		self.dist = inf
		self.parent = self.child = -1
		self.neighbors = list()
		self.distances = dict()

	# Less Than function used by Heapq for determining priority
	def __lt__(self, other):
		return self.dist < other.dist

	# Stores new neighbor and pre-processes the distance to it
	def add_neighbor(self, n, d=None):
		self.neighbors.append(n)

		if d is None:  # Calculates and returns distance between nodes if not already known
			dist = self.distance(Vertex.all_nodes.get(n))
			self.distances[n] = dist
			return dist
		else:  # If distance is already known, simply set it and return nothing
			self.distances[n] = d

	# Deprecated
	def remove_neighbor(self, n):
		self.neighbors.remove(n)

	# Calculate distance between self and other node
	def distance(self, other):
		delta_x = abs(self.x - other.x)
		delta_y = abs(self.y - other.y)
		return sqrt((delta_x ** 2) + (delta_y ** 2))

	# Return distance of self to neighbor
	def get_dist(self, n):
		return self.distances[n]
