from app.services.embeddings import EmbeddingService
from app.services.vectorstore import VectorStore
from app.core.config import settings

embedder = EmbeddingService(settings.EMBEDDING_MODEL)

def policy_mapping_node(state):
    internal_chunks = state["internal_chunks"]

    vectorstore = VectorStore(collection_name="internal_policy")

    internal_embeddings = embedder.embed(internal_chunks)
    vectorstore.add_documents(internal_chunks, internal_embeddings)

    mapped = []

    for req in state["extracted_requirements"]:
        req_embedding = embedder.embed([req["text"]])[0]
        results = vectorstore.search(req_embedding)

        matches = []
        for doc, score in zip(
            results["documents"][0],
            results["distances"][0]
        ):
            matches.append({
                "text": doc,
                "score": round(1 - score, 3)
            })

        mapped.append({
            "requirement": req,
            "matches": matches
        })

    state["mapped_policies"] = mapped
    return state
