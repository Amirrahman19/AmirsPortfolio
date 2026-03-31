import dash
from dash import html
import dash_cytoscape as cyto
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# =========================
# REAL SYSTEM GRAPH
# =========================
graph_data = {

    # ROOT
    "JARVISS System": [
        "JARVISS Core",
        "HIVE System"
    ],

    # =========================
    # JARVISS CORE (REAL FUNCTIONS)
    # =========================
    "JARVISS Core": [
        "System Orchestrator",
        "Decision Engine",
        "Model Management",
        "Access Control System"
    ],

    "Decision Engine": [
        "Threat Assessment",
        "Confidence Evaluation",
        "Response Logic"
    ],

    "Model Management": [
        "Model Upload",
        "Model Selection",
        "Version Control"
    ],

    "Access Control System": [
        "Controller Interface",
        "Supervisor Interface",
        "Developer Interface"
    ],

    # =========================
    # HIVE SYSTEM (PIPELINE)
    # =========================
    "HIVE System": [
        "Phase 1 - Foundation",
        "Phase 2 - Scaling",
        "Phase 3 - Awareness",
        "Phase 4 - Intelligence Platform"
    ],

    # -------- PHASE 1
    "Phase 1 - Foundation": [
        "Dataset Collection Node",
        "Annotation Node",
        "Baseline Detection Node"
    ],

    "Dataset Collection Node": [
        "Maritime Footage",
        "Phone Capture Input"
    ],

    "Annotation Node": [
        "Bounding Boxes",
        "Segmentation Labels"
    ],

    "Baseline Detection Node": [
        "YOLOv8 Training",
        "Initial Model Weights"
    ],

    # -------- PHASE 2
    "Phase 2 - Scaling": [
        "Multi-Class Detection Node",
        "Dataset Scaling Node",
        "Training Pipeline Node"
    ],

    "Multi-Class Detection Node": [
        "Person Detection",
        "Vessel Classes (Kayak, Sampan, Speedboat)"
    ],

    "Dataset Scaling Node": [
        "Pseudo-Labeling",
        "Auto Annotation"
    ],

    "Training Pipeline Node": [
        "YOLOv8m Training",
        "Batch Processing"
    ],

    # -------- PHASE 3
    "Phase 3 - Awareness": [
        "Swimmer Detection Node",
        "Vessel Detection Node",
        "Wave Analysis Node",
        "Multi-Modal Input Node"
    ],

    "Wave Analysis Node": [
        "Wake Detection",
        "Ripple Detection",
        "Wave Pattern Differentiation"
    ],

    "Multi-Modal Input Node": [
        "RGB Camera Feed",
        "Thermal Camera Feed"
    ],

    # -------- PHASE 4
    "Phase 4 - Intelligence Platform": [
        "Fusion Engine Node",
        "Verification Node",
        "Active Learning Node",
        "Live Inference Node",
        "Video Upload Node"
    ],

    "Fusion Engine Node": [
        "RGB + Thermal Fusion",
        "Multi-Model Integration"
    ],

    "Verification Node": [
        "Wave + Object Cross-Check",
        "Confidence Filtering"
    ],

    "Active Learning Node": [
        "Error Feedback Loop",
        "Retraining Pipeline"
    ],

    "Live Inference Node": [
        "Real-Time Detection",
        "Bounding Box Rendering"
    ]
}

# =========================
# STATE
# =========================
expanded_nodes = set(["JARVISS System"])

# =========================
# GRAPH GENERATION
# =========================
def generate_elements():
    elements = []
    visited = set()

    def dfs(node, parent=None):
        if node in visited:
            return
        visited.add(node)

        elements.append({"data": {"id": node, "label": node}})

        if parent:
            elements.append({"data": {"source": parent, "target": node}})

        if node in expanded_nodes:
            for child in graph_data.get(node, []):
                dfs(child, node)

    dfs("JARVISS System")
    return elements

# =========================
# UI
# =========================
app.layout = html.Div([
    html.H2("JARVISS + HIVE Real System Architecture", style={'textAlign': 'center'}),

    cyto.Cytoscape(
        id='graph',
        layout={
            'name': 'breadthfirst',
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
                    'text-max-width': 140,
                    'font-size': '13px',
                    'background-color': '#2ECC40',
                    'color': 'black',
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
                    'background-color': '#FF4136'
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
    app.run(debug=False, port=8051)