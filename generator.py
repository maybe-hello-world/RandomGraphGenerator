import random
import math

def generate(node_number, fully_connected = True, density = 50,
             weights = True, weight_min = 1, weight_max = 100,
             multi_edges = False, self_connections = False, oriented = True):
	"""
	Generate random graph

	:param node_number: Number of nodes
	:param weights: If to generate weights (bool)
	:param fully_connected: if graph fully connected (bool)
	:param density: percent of density (0 < int < 100)
	:param weight_min: minimal number of weights
	:param weight_max: maximum number of weights
	:param multi_edges: if there can be multi edges from one node to another
	:param self_connections: if there can be edge from node to itself
	:param oriented: if graph oriented
	:return: list of tuples (node1, node2, weight)
	"""
	r = random.Random()
	answer = []
	if fully_connected:
		for i in range(node_number):
			answer.append((i, i + 1))

	while len(answer) / node_number ** 2 < density / 100:
		# add new edge
		flag = True
		edge = (
			int(math.floor(r.uniform(0, node_number + 1))),
			int(math.floor(r.uniform(0, node_number + 1)))
		)

		# check multi connections
		if not multi_edges:
			if edge in answer:
				flag = False

		# check self connections
		if not self_connections:
			if edge[0] == edge[1]:
				flag = False

		# check for orientation
		if not oriented:
			if (edge[1], edge[0]) in answer:
				flag = False

		if flag:
			answer.append(edge)

	# add weights
	if weights:
		answer = [(i[0], i[1], int(r.uniform(weight_min, weight_max))) for i in answer]

	return answer