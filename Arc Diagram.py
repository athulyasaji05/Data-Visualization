import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

G = nx.Graph()
edges = [(0, 1), (0, 2), (1, 2), (1, 3), (3, 4), (2, 4)]
G.add_edges_from(edges)

# Define node positions in a circular layout
pos = {i: (np.cos(2 * np.pi * i / len(G.nodes)), np.sin(2 * np.pi * i / len(G.nodes))) for i in G.nodes}

# Create the plot
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10, edge_color='gray')

# Draw the arcs
for u, v in G.edges():
    x = np.linspace(pos[u][0], pos[v][0], 100)
    y = np.linspace(pos[u][1], pos[v][1], 100)
    plt.plot(x, y, color='gray', alpha=0.7)
