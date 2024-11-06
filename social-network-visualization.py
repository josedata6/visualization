import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx


# visualize a simple connections among nodes
G1 = nx.DiGraph()
# define nodes
G1.add_node(1)
G1.add_node(2)
G1.add_node(3)
G1.add_node(4)
G1.add_node(5)
# add edges
G1.add_edge(1,2)
G1.add_edge(1,3)
G1.add_edge(1,4)
G1.add_edge(5,4)
G1.add_edge(1,5)


# setup the layout of the network structure
pos = nx.spring_layout(G1)
# draw the nodes
nx.draw_networkx_nodes(G1, pos, node_color="#8ac926", node_size=500)
# draw the edge
nx.draw_networkx_edges(G1, pos, edge_color="#7f5539")
#draw labels
nx.draw_networkx_labels(G1, pos)
plt.show()

# task draw a network that contains three nodes (a, b, 1). They all connected to each other
# G3 is your network name
G3 = nx.DiGraph()
# define nodes
G3.add_node('a')
G3.add_node('b')
G3.add_node(1)

# add edges
G3.add_edge('a','b')
G3.add_edge('a',1)
G3.add_edge('b',1)

# setup the layout of the network structure
pos = nx.spring_layout(G3)
# draw the nodes
nx.draw_networkx_nodes(G3, pos, node_color="#8ac926", node_size=500)
# draw the edge
nx.draw_networkx_edges(G3, pos, edge_color="#7f5539", arrows=False)
#draw labels
nx.draw_networkx_labels(G3, pos)
plt.show()

df = pd.read_csv('social_media.csv')
df.head()

# create an empty graph
G2 = nx.DiGraph()
# assign nodes and edges from dataframe for G2
G2 = nx.from_pandas_edgelist(df, source='user_name', target='follows_who',
                             edge_attr='days')

# print nodes
nodelist = G2.nodes()
nodelist

# extract edges
G2.edges()

# strenghts of the friendship
weights = list(nx.get_edge_attributes(G2, 'days').values())
print(weights)
new_weights = [i/50 for i in weights]
print(new_weights)

# find degree information
degree_info = nx.degree(G2)
print(degree_info)
scaled_degree = [degree_info[1]*1000 for degree_info in nx.degree(G2)]
scaled_degree

# setup the layout
pos = nx.spring_layout(G2)
nx.draw_networkx_nodes(G2, pos, node_color=scaled_degree, cmap='spring',
                       node_size=scaled_degree)
nx.draw_networkx_edges(G2, pos, width=new_weights)
nx.draw_networkx_labels(G2, pos)
plt.show()