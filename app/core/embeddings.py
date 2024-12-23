from transformers import AutoModel, AutoTokenizer
import torch
import numpy as np

def generate_embeddings(text: str):
    tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
    model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

    MAX_LENGTH = 512
    inputs = tokenizer(text, padding=True, truncation=True, max_length=MAX_LENGTH, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    last_hidden_states = outputs.last_hidden_state

    cls_embeddings = last_hidden_states[:, 0, :].squeeze().cpu().numpy()

    token_embeddings = last_hidden_states.squeeze().cpu().numpy()
    avg_embeddings = np.mean(token_embeddings, axis=0)

    return avg_embeddings.tolist()
