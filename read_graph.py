import networkx as nx
import sys


filename = sys.argv[1]

# G = nx.path_graph(4)
# nx.write_adjlist(G, "test.adjlist")

G = nx.read_adjlist(filename)
print('number of nodes: ', G.number_of_nodes())
print('number of edges: ', G.number_of_edges())
# nx.draw(G)
# plt.savefig(filename + '_plot.png')

