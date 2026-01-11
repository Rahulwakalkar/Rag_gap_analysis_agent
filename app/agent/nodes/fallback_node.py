from datetime import datetime

def report_node(state):
    state["final_report"] = {
        "analysis_metadata": {
            "analysis_date": datetime.utcnow().isoformat(),
            "agent_version": "1.0.0"
        },
        "executive_summary": {
            "total_requirements": len(state["extracted_requirements"]),
            "gaps_identified": len(state["gaps"]),
            "critical_gaps": sum(1 for g in state["gaps"] if g["severity"] == "critical")
        },
        "gaps": state["gaps"]
    }
    return state
