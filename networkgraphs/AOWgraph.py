import networkx as nx
from pyvis.network import Network

# =========================
# GRAPH SETUP
# =========================
G = nx.DiGraph()

CENTER = "The Art of War"
G.add_node(CENTER, level=0, title="Ancient strategy system by Sun Tzu")

# Layer 1
layer1 = {
    "Core Principles": {
        "Know Yourself & Enemy": "Understand strengths, weaknesses, data",
        "Deception": "Mislead, hide intent, indirect methods",
        "Win Without Fighting": "Avoid unnecessary conflict",
        "Speed & Flexibility": "Adapt quickly to change"
    },
    "Strategies & Tactics": {
        "Outsmart Not Outfight": "Efficiency over brute force",
        "Adaptation": "Dynamic strategy",
        "Indirect Force": "Use secondary methods",
        "Context Matters": "No fixed rules"
    }
}

# Add nodes
for parent, children in layer1.items():
    G.add_node(parent, level=1, title=parent)
    G.add_edge(CENTER, parent)

    for child, desc in children.items():
        G.add_node(child, level=2, title=desc)
        G.add_edge(parent, child)

# =========================
# DEEP LAYER
# =========================
deep = {
    "Deception": {
        "Mask Intent": "Hide true objective",
        "False Signals": "Create misleading patterns"
    },
    "Know Yourself & Enemy": {
        "Self Analysis": "Evaluate internal capability",
        "Opponent Analysis": "Understand external threats"
    },
    "Adaptation": {
        "Dynamic Change": "Adjust in real time",
        "Feedback Loop": "Learn and improve"
    }
}

for parent, children in deep.items():
    for child, desc in children.items():
        G.add_node(child, level=3, title=desc)
        G.add_edge(parent, child)

# =========================
# VISUALISE
# =========================
net = Network(height="800px", width="100%", directed=True)

for node in G.nodes():
    level = G.nodes[node]["level"]

    color = ["red", "orange", "green", "blue"][level]
    size = [35, 25, 18, 12][level]

    net.add_node(
        node,
        label=node,
        title=G.nodes[node].get("title", ""),
        color=color,
        size=size
    )

for edge in G.edges():
    net.add_edge(edge[0], edge[1])

# Physics + smooth interaction
net.set_options("""
var options = {
  "physics": {
    "barnesHut": {
      "gravitationalConstant": -2500,
      "springLength": 180
    }
  },
  "interaction": {
    "hover": true,
    "navigationButtons": true,
    "keyboard": true
  }
}
""")

net.write_html("aow_simple_graph.html")
print("Generated: aow_simple_graph.html")