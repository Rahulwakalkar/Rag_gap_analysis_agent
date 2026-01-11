from app.agent.tools.search import semantic_search

def map_policies(state):
    mappings = []

    for req in state["extracted_requirements"]:
        matches = semantic_search(
            req["text"],
            state["internal_chunks"]
        )

        mappings.append({
            "requirement": req,
            "coverage": matches
        })

    state["mapped_policies"] = mappings
    return state
