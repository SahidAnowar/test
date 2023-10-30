from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = FastAPI()

# Load the GPT-Neo 1.3B model from HuggingFace
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")

model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B")

@app.post("/generate")
async def generate(prompt: str):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(input_ids, max_length=100, num_return_sequences=1)

    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return {"response": response}
