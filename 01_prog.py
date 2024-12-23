import networkx as nx
import matplotlib.pyplot as plt
import random
def create_wireless_topology(num_nodes, area_size, connection_range):
    G = nx.Graph()
    positions = {i: (random.uniform(0, area_size), random.uniform(0, area_size)) for i in range(num_nodes)}
    nx.set_node_attributes(G, positions, 'pos')
    G.add_nodes_from(positions.keys())
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            dist = ((positions[i][0] - positions[j][0])**2 + (positions[i][1] - positions[j][1])**2)**0.5
            if dist <= connection_range:
                G.add_edge(i, j)
    return G, positions
num_nodes = 10  # Number of devices
area_size = 100  # Area size (100x100)
connection_range = 30  # Maximum connection range
G, positions = create_wireless_topology(num_nodes, area_size, connection_range)
plt.figure(figsize=(10, 10))
nx.draw(
    G, pos=positions, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray', font_size=10
)
plt.title("Wireless Network Topology")
plt.show()
