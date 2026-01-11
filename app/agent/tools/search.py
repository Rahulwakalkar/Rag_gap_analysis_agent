import numpy as np
from typing import List

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def semantic_search(query_emb, doc_embs, docs, threshold=0.75):
    results = []
    for emb, doc in zip(doc_embs, docs):
        score = cosine_similarity(query_emb, emb)
        if score >= threshold:
            results.append({"text": doc, "score": float(score)})
    return sorted(results, key=lambda x: x["score"], reverse=True)
