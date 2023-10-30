from fastapi import FastAPI
from transformers import DollyProcessor, DollyImageChatModel

app = FastAPI()

# Print the version of the transformers library
import transformers
print("Transformers library version:", transformers.__version__)

try:
    # Load Dolly v2 3b model from HuggingFace
    model = DollyImageChatModel.from_pretrained("databricks/dolly-v2-3b")
    processor = DollyProcessor.from_pretrained("databricks/dolly-v2-3b")
except Exception as e:
    print("Error loading the model:", str(e))

@app.post("/generate")
async def generate(prompt: str):
    inputs = processor(prompt, return_tensors="pt")
    out = model.generate(**inputs)
    response = processor.decode(out[0])
    return {"response": response}
