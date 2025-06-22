from sentence_transformers import SentenceTransformer, util
import torch

model = SentenceTransformer("jinaai/jina-embeddings-v2-base-en")

def classify_paper(text, topics):
    paper_embedding = model.encode(text, convert_to_tensor=True)
    topic_embeddings = model.encode(topics, convert_to_tensor=True)
    similarities = util.pytorch_cos_sim(paper_embedding, topic_embeddings)[0]
    best_idx = torch.argmax(similarities).item()
    return topics[best_idx]
