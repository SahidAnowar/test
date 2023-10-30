from fastapi import FastAPI
from transformers import DollyProcessor, DollyImageChatModel

app = FastAPI()

# Load Dolly v2 3b model from HuggingFace
model = DollyImageChatModel.from_pretrained("databricks/dolly-v2-3b")
processor = DollyProcessor.from_pretrained("databricks/dolly-v2-3b")

@app.post("/generate")
async def generate(prompt: str):
    inputs = processor(prompt, return_tensors="pt")
    out = model.generate(**inputs)
    response = processor.decode(out[0])
    return {"response": response}
