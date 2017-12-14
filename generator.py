import random
import math


def __dense_generation(answer, node_number, oriented, self_connections, fully_connected, density):
	# generate initial possible values
	if oriented:
		initial = [(i, k)
			       for i in range(node_number)
			       for k in range(node_number)]
	else:
		initial = [(i, k)
			       for i in range(node_number)
			       for k in range(i, node_number)]

	# remove self connections if needed
	if not self_connections:
		for i in range(node_number):
			initial.remove((i, i))

	# create first full connected chain if needed
	if fully_connected:
		for i in range(node_number - 1):
			answer.append((i, i + 1))
			initial.remove((i, i + 1))

	# determine number of edges to add
	num_range = int((node_number ** 2) * (density / 100) + 1 - len(answer))
	if len(initial) < num_range:
		num_range = len(initial)

	for i in range(num_range):
		# select new edge
		r_number = int(random.uniform(0, len(initial)))

		# transfer edge from potential edges to real
		edge = initial.pop(r_number)
		answer.append(edge)


def __sparse_generation(answer, node_number, oriented, self_connections, fully_connected, density):
	if fully_connected:
		for i in range(node_number):
			answer.append((i, i + 1))

	counter = 0
	divisor = (100 / (node_number ** 2) / density)
	while counter * divisor < 0.95:
		# add new edge
		flag = True
		edge = (
			int(math.floor(random.uniform(0, node_number + 1))),
			int(math.floor(random.uniform(0, node_number + 1)))
		)

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
			counter += 1
			print(counter * divisor)


def generate(node_number, fully_connected = True, density = 50,
             weights = True, weight_min = 1, weight_max = 100,
             self_connections = False, oriented = True):
	"""
	Generate random graph

	:param node_number: Number of nodes
	:param weights: If to generate weights (bool)
	:param fully_connected: if graph fully connected (bool)
	:param density: percent of density (0 < int < 100)
	:param weight_min: minimal number of weights
	:param weight_max: maximum number of weights
	:param self_connections: if there can be edge from node to itself
	:param oriented: if graph oriented
	:return: list of tuples (node1, node2, weight)
	"""
	answer = []

	if density > 50:
		__dense_generation(answer, node_number, oriented, self_connections, fully_connected, density)
	else:
		__sparse_generation(answer, node_number, oriented, self_connections, fully_connected, density)
	print("generated")

	# add weights
	if weights:
		for i in range(len(answer)):
			answer[i] = (answer[i][0], answer[i][1], int(random.uniform(weight_min, weight_max)))

	return answer