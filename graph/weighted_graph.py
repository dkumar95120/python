from collections import defaultdict

class Graph():
	def __init__(self):
		# each edge to store neighbors of the key node as a list e.g.
		# {'a': ['b','c','d']}
		# 
		self.edges = defaultdict(list)
		# distances for each edge would be stored as
		# {('a','b'): 6}
		self.distance = {}

	def add_edge (self, src_node, dst_node, distance):
		self.edges[src_node].append(dst_node)
		self.edges[dst_node].append(src_node)
		self.distance[(src_node,dst_node)] = distance	
		self.distance[(dst_node,src_node)] = distance

	def shortest_distance(self, start, end):
		min_path = {start: (None, 0)}
		cur_node = start
		visited = set()

		while cur_node != end:
			visited.add(cur_node)
			neighbors = self.edges[cur_node]
			distance_to_cur_node = min_path[cur_node][1]

			for next_node in neighbors:
				# find cumulative distance to the neighbor
				distance = self.distance[(cur_node,next_node)] + distance_to_cur_node
				if next_node not in min_path:
					min_path[next_node] = (cur_node, distance)
				else:
					cur_shortest_distance = min_path[next_node][1]
					if cur_shortest_distance > distance:
						min_path[next_node] = (cur_node, distance)

			next_neighbors = {node: min_path[node] for node in min_path if node not in visited}

			if not bool(next_neighbors):
				return -1

			# next node is the one with the shortest distance among next neighbors
			cur_node = min(next_neighbors, key=lambda k: next_neighbors[k][1])

		# back trace path through min_path
		path = []
		distance = 0
		while bool(cur_node):
			path.append(cur_node)
			next_node = min_path[cur_node][0]
			if distance == 0:
				distance += min_path[cur_node][1]
			cur_node = next_node

		#reverse path
		path = path[::-1]
		print (path)
		return distance

