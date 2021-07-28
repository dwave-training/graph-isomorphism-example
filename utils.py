import itertools
import numpy as np
import networkx as nx

# Ignore errors importing matplotlib.pyplot (may not be available in
# testing framework)
try:
    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors
except ImportError:
    pass

import dimod
from dwave.system import LeapHybridDQMSampler


# Directly taken from https://github.com/dwave-examples/circuit-equivalence
def plot_graphs(G1, G2, node_mapping):
    """Plot graphs of two circuits
    The provided mapping specifies how nodes in graph 1 correspond to
    nodes in graph 2.  The nodes in each graph are colored using
    matching colors based on the specified mapping.
    Args:
        G1 (networkx.Graph)
        G2 (networkx.Graph)
        node_mapping (dict):
            Dictionary that defines the correspondence between nodes
            in graph 1 and nodes in graph 2.  The keys are names of
            nodes in graph 1, and the values are names of nodes in
            graph 2.
    """
    f, axes = plt.subplots(1, 2, figsize=[15,7.5])

    colors = itertools.cycle(mcolors.TABLEAU_COLORS)
    G1_colors = [c for c,i in zip(colors, G1.nodes)]
    G2_targets = [node_mapping[n] for n in G1.nodes]
    G2_colors = [G1_colors[G2_targets.index(n)] for n in G2.nodes]

    nx.draw(G1, with_labels=True, ax=axes[0], node_color=G1_colors)
    nx.draw(G2, with_labels=True, ax=axes[1], node_color=G2_colors)
