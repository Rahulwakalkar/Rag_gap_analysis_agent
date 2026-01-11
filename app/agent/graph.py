from langgraph.graph import StateGraph
from app.agent.state import AgentState
from app.agent.nodes.llm_node import requirement_extraction_node
from app.agent.nodes.tool_node import policy_mapping_node
from app.agent.nodes.router_node import gap_detection_node
from app.agent.nodes.fallback_node import report_node

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("extract", requirement_extraction_node)
    graph.add_node("map", policy_mapping_node)
    graph.add_node("gap", gap_detection_node)
    graph.add_node("report", report_node)

    graph.set_entry_point("extract")
    graph.add_edge("extract", "map")
    graph.add_edge("map", "gap")
    graph.add_edge("gap", "report")

    return graph.compile()
