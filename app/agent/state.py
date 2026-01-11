from typing import List, Dict, Any
from typing_extensions import TypedDict

class AgentState(TypedDict):
    regulatory_text: str
    internal_text: str
    regulatory_chunks: List[str]
    internal_chunks: List[str]
    extracted_requirements: List[Dict[str, Any]]
    mapped_policies: List[Dict[str, Any]]
    gaps: List[Dict[str, Any]]
    final_report: Dict[str, Any]
