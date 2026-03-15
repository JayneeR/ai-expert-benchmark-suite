from fastapi import FastAPI
import torch

app = FastAPI(title="AI Expert Benchmark API")

@app.post("/evaluate")
async def evaluate_alignment(response_vec: list, expert_vec: list):
    u = torch.tensor(response_vec)
    v = torch.tensor(expert_vec)
    score = torch.nn.functional.cosine_similarity(u, v, dim=0)
    return {"expert_alignment_score": float(score)}
