import dash
from dash import html
import dash_cytoscape as cyto
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# =========================
# GRAPH DATA (SONARA)
# =========================
graph_data = {
    "Sonara Global": [
        "Mental Wellness",
        "Personal Growth",
        "AI & Humanity",
        "Community & Impact",
        "Content & Education"
    ],

    "Mental Wellness": [
        "Emotional Awareness",
        "Stress Management",
        "Support Systems"
    ],

    "Personal Growth": [
        "Discipline",
        "Identity",
        "Purpose"
    ],

    "AI & Humanity": [
        "Ethical AI",
        "Human-AI Balance",
        "Future of Work"
    ],

    "Community & Impact": [
        "Volunteering",
        "Events",
        "Partnerships"
    ],

    "Content & Education": [
        "Podcast",
        "Articles",
        "Workshops"
    ],

    # =========================
    # DEEP LAYER
    # =========================
    "Emotional Awareness": [
        "Journaling",
        "Reflection",
        "Self-Understanding"
    ],

    "Discipline": [
        "Habit Systems",
        "Consistency",
        "Routine Building"
    ],

    "Ethical AI": [
        "Bias Awareness",
        "Responsible AI",
        "Transparency"
    ],

    "Podcast": [
        "Guest Speakers",
        "Storytelling",
        "Real Conversations"
    ],

    "Volunteering": [
        "Mental Health Campaigns",
        "Youth Outreach",
        "Community Service"
    ]
}

expanded_nodes = set(["Sonara Global"])

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

    dfs("Sonara Global")
    return elements

# =========================
# UI
# =========================
app.layout = html.Div([
    html.H2("Sonara Global System Map", style={'textAlign': 'center'}),

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
                    'text-max-width': 100,
                    'font-size': '14px',
                    'background-color': '#6A0DAD',  # 🔥 Sonara purple vibe
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
                    'background-color': '#FF851B',
                    'line-color': '#FF851B',
                    'target-arrow-color': '#FF851B'
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
    app.run(debug=False, port=8052)