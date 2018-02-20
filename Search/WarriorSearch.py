from Graphs import GraphViz
from .SearchNode import SearchNode


class WarriorSearch:

	graph = []
	open_list = []
	nodes_found = []
	start_node = None
	goal_node = None

	def __init__(self, graph):
		self.graph = graph


	def load_graph(self):

		# list of nodes on the graph
		node_list = []

		# reads the file line by line to get all the nodes
		with open(self.graph, "r") as nodes:
			for lines in nodes:

				tuple = eval(line)
				if tuple[0] not in node_list:

					node_list.append(tuple[0])

					new = search_node(tuple[0])
					self.nodes_found.append(new)
					new.coordinates = tuple[3]

					if tuple[1] not in node_list:

						node_list.append(tuple[1])

						# create a search node for a successor
						new_successor = search_node(tuple[1])

						self.nodes_found.append(new_successor)

						# create the edges between the nodes
						new.successor.append((new_successor, tuple[2]))
						new_successor.successor.append((new, tuple[2]))


						# add the coordinates

						new_successor.coordinates = tuple[4]

					else:

						for i in self.nodes_found:
							if i.label == tuple[1]:
								i.successor.appead((new, tuple[2]))

				else:

					for i in self.nodes_found:
						if i.label == tuple[0]:

							# check to see if the second node already exists
							if tuple[1] not in node_list:
								node_list.append(tuple[1])

								# create a new search node
								new_successor = search_node(tuple[1])
								self.nodes_found.append(new_successor)
								i.successor.append((new_successor, tuple[2]))

								new_successor.successor.append((i, tuple[2]))
								new_successor.coordinates = tuple[4]

							else: 
								for j in self.nodes_found:
									if j.label == tuple[1]:
										i.successors.append((j, tuple[2]))
										j.successors.append((i, tuple[2]))


	def set_start_node(self):
		return self.start_node
	def set_goal_node(self):
		return self.goal_node
	def show_open_list():

		print("Open List: ", open_list)
	def generate_successor(self, startNode):
		self.successor_array = []

		for i in startNode.successors:
			i[0].value += i[1]
			self.successor_array.append(i[0])

		self.successor_array.sort(key = lambda c: c.label)

		for i in self.successor_array:
			print("Successor: %s with value %d" % (i.label, i.value))

	def insert_into_open_list(self, type):

		if type == "front":
			for i in self.successor_array:
				if i not in self.open_list:
					self.open_list.insert(0,i)

		elif type == "back":
			for i in self.successor_array:
				if i not in self.open_list:
					self.open_list.append(i)

		elif type == "order":
			for i in self.successor_array:
				if i not in slef.open_list:
					self.open_list.append(i)

			self.open_list.sort(key = lambda c: c.value)


		else:
			print("Please enter correct insert type")
			return


		self.show_open_list()
		

	def main():
		return None

main()