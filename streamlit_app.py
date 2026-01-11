import streamlit as st
from app.agent.graph import build_graph
from app.services.document_loader import load_pdf_text, chunk_text
import traceback

st.set_page_config("AI Policy Gap Analysis Agent", layout="wide")
st.title("AI Policy Gap Analysis Agent")

regulatory_file = st.file_uploader(
    "Upload Regulatory Policy (PDF)",
    type=["pdf"]
)

internal_file = st.file_uploader(
    "Upload Internal Policy (PDF)",
    type=["pdf"]
)

if regulatory_file and internal_file:
    regulatory_text = load_pdf_text(regulatory_file)
    internal_text = load_pdf_text(internal_file)

    regulatory_chunks = chunk_text(regulatory_text)
    internal_chunks = chunk_text(internal_text)

    if st.button("Run Gap Analysis"):
        try:
            graph = build_graph()
            result = graph.invoke({
                "regulatory_text": regulatory_text,
                "internal_text": internal_text,
                "regulatory_chunks": regulatory_chunks,
                "internal_chunks": internal_chunks,
                "extracted_requirements": [],
                "mapped_policies": [],
                "gaps": [],
                "final_report": {}
            })

            st.subheader("Gap Analysis Report")
            st.json(result["final_report"])

        except Exception:
            st.error("Agent execution failed")
            st.code(traceback.format_exc())
else:
    st.info("Upload both PDF documents to proceed.")
