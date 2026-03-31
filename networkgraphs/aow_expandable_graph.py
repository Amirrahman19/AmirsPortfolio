import dash
from dash import html
import dash_cytoscape as cyto
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# =========================
# GRAPH DATA
# =========================
graph_data = {
    "The Art of War": ["Core Principles", "Strategies"],

    "Core Principles": [
        "Know Yourself & Enemy",
        "Deception",
        "Win Without Fighting"
    ],

    "Strategies": [
        "Adaptation",
        "Indirect Force"
    ],

    "Know Yourself & Enemy": ["Self Analysis", "Opponent Analysis"],
    "Deception": ["Mask Intent", "False Signals"],
    "Adaptation": ["Dynamic Change", "Feedback Loop"]
}

expanded_nodes = set(["The Art of War"])

# =========================
# GENERATE GRAPH
# =========================
def generate_elements():
    elements = []
    visited = set()

    def dfs(node, parent=None):
        if node in visited:
            return
        visited.add(node)

        elements.append({
            "data": {"id": node, "label": node}
        })

        if parent:
            elements.append({
                "data": {"source": parent, "target": node}
            })

        if node in expanded_nodes:
            for child in graph_data.get(node, []):
                dfs(child, node)

    dfs("The Art of War")
    return elements

# =========================
# UI
# =========================
app.layout = html.Div([
    html.H2("Expandable Art of War Graph", style={'textAlign': 'center'}),

    cyto.Cytoscape(
        id='graph',
        layout={
            'name': 'breadthfirst',   # 🔥 MUCH cleaner layout
            'directed': True,
            'padding': 20,
            'spacingFactor': 1.5
        },
        style={'width': '100%', 'height': '90vh'},
        elements=generate_elements(),

        stylesheet=[
            {
                'selector': 'node',
                'style': {
                    'label': 'data(label)',
                    'text-wrap': 'wrap',
                    'text-max-width': 100,
                    'font-size': '14px',
                    'background-color': '#0074D9',
                    'color': 'white',
                    'text-valign': 'center',
                    'text-halign': 'center',
                    'width': 'label',
                    'height': 'label',
                    'padding': '10px'
                }
            },
            {
                'selector': 'edge',
                'style': {
                    'curve-style': 'bezier',
                    'target-arrow-shape': 'triangle',
                    'line-color': '#aaa',
                    'target-arrow-color': '#aaa'
                }
            },
            {
                'selector': ':selected',
                'style': {
                    'background-color': '#FF4136',
                    'line-color': '#FF4136',
                    'target-arrow-color': '#FF4136'
                }
            }
        ]
    )
])

# =========================
# CLICK EXPAND
# =========================
@app.callback(
    Output('graph', 'elements'),
    Input('graph', 'tapNodeData')
)
def expand_node(node_data):
    if not node_data:
        return generate_elements()

    node_id = node_data['id']

    if node_id in expanded_nodes:
        expanded_nodes.remove(node_id)
    else:
        expanded_nodes.add(node_id)

    return generate_elements()

# =========================
# RUN
# =========================
if __name__ == '__main__':
    app.run(debug=True)