from app.agent.state import AgentState

def test_state_keys():
    state = AgentState(
        regulatory_text="",
        internal_text="",
        extracted_requirements=[],
        mapped_policies=[],
        gaps=[],
        final_report={}
    )
    assert "regulatory_text" in state
