# Imports
from search import WarriorSearch
from search import SearchNode

# Test GraphSearch

# Initialize graph search
print("Loading graph file")
ws = WarriorSearch("test_data/30.txt")
print("Graph loaded:", ws.graph)

# Set goals
ws.set_start_node("U")
ws.set_goal_node("T")
ws.show_open_list()

# Generate successors
successors = ws.generate_successors(gs.open_list[0])
print("'U' Successors:", successors)

# Insert successors and re-show open
ws.insert_into_open_list(successors, "order")
ws.show_open_list()

# Test duplicates
ws.insert_into_open_list([SearchNode("K", 500),
                 SearchNode("C", 19),
                 SearchNode("J", 10)])
ws.show_open_list()