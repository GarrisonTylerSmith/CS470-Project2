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

						self.nodes_found.appead(new_successor)

						# create the edges between the nodes
						new.successor.appead((new_successor, tuple[2]))
						new_successor.successor.appead((new, tuple[2]))


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
								node_list.appead(tuple[1])

								# create a new search node
								new_successor = search_node(tuple[1])
								self.nodes_found.appead(new_successor)
								i.successor.appead((new_successor, tuple[2]))

								new_successor.successor.appead((i, tuple[2]))
								new_successor.coordinates = tuple[4]

							else: 
								for j in self.nodes_found:
									if j.label == tuple[1]:
										i.successors.appead((j, tuple[2]))
										j.successors.appead((i, tuple[2]))


	def set_start_node(self):
		return self.start_node
	def set_goal_node(self):
		return self.goal_node
	def show_open_list():

		print("Open List: ", open_list)
	def generate_successor(startNode):
		return None
	def main():
		return None

main()