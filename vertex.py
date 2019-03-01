from math import sqrt


class Vertex:

	all_nodes = dict()
	id = 0

	def __init__(self, x, y):
		Vertex.all_nodes[Vertex.id] = self
		Vertex.id += 1
		self.x = x
		self.y = y
		self.neighbors = list()
		self.distances = dict()

	def add_neighbor(self, n, d=None):
		self.neighbors.append(n)
		if d is None:
			dist = self.distance(Vertex.all_nodes.get(n))
			self.distances[n] = dist
			return dist
		else:
			self.distances[n] = d

	def distance(self, other):
		delta_x = abs(self.x - other.x)
		delta_y = abs(self.y - other.y)
		return sqrt((delta_x ^ 2) + (delta_y ^ 2))
