# src/visualization.py
import networkx as nx
import matplotlib.pyplot as plt

def visualize_dependencies(dependencies):
    G = nx.DiGraph()
    for task in dependencies.keys():
        G.add_node(task)
    for task, deps in dependencies.items():
        for dep in deps:
            G.add_edge(dep, task)
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, seed=42)
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color="lightblue")
    nx.draw_networkx_edges(G, pos, width=1.5, arrows=True, arrowstyle='-|>', arrowsize=20)
    nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
    plt.title("Task Dependencies", size=15)
    plt.axis("off")
    plt.tight_layout()
    plt.show()
