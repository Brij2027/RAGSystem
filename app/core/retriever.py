from scipy.spatial.distance import cosine

def retrieve_similar(query_embedding, document_embeddings):
    similarities = [
        (doc_id, 1 - cosine(query_embedding, doc_emb))
        for doc_id, doc_emb in document_embeddings
    ]

    return sorted(similarities, key=lambda x: x[1], reverse=True)[:5]