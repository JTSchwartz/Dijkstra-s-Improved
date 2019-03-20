from math import sqrt, inf


class Vertex:

	all_nodes = dict()

	def __init__(self, id_num, x, y):
		Vertex.all_nodes[id_num] = self
		self.id = id_num
		self.x = x
		self.y = y
		self.dist = inf
		self.parent = self.child = -1
		self.neighbors = list()
		self.distances = dict()

	def __lt__(self, other):
		return self.dist < other.dist

	def add_neighbor(self, n, d=None):
		self.neighbors.append(n)
		if d is None:
			dist = self.distance(Vertex.all_nodes.get(n))
			self.distances[n] = dist
			return dist
		else:
			self.distances[n] = d

	# Deprecated
	def remove_neighbor(self, n):
		self.neighbors.remove(n)

	def distance(self, other):
		delta_x = abs(self.x - other.x)
		delta_y = abs(self.y - other.y)
		return sqrt((delta_x ** 2) + (delta_y ** 2))

	def get_dist(self, n):
		return self.distances[n]
