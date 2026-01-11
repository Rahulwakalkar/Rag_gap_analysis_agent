def gap_detection_node(state):
    gaps = []

    for item in state["mapped_policies"]:
        matches = item["matches"]
        status = "missing" if not matches else "partial"

        severity = "critical" if status == "missing" else "medium"

        gaps.append({
            "regulatory_reference": item["requirement"],
            "internal_coverage": {
                "status": status,
                "related_sections": [m["text"] for m in matches],
                "coverage_text": matches[0]["text"] if matches else None
            },
            "severity": severity,
            "confidence_score": matches[0]["score"] if matches else 0.0,
            "recommendation": "Update internal policy to address this requirement."
        })

    state["gaps"] = gaps
    return state
