from fastapi import FastAPI
from dotenv import load_dotenv
import os
from openai import OpenAI
import os


app = FastAPI()
load_dotenv()

# خواندن کلید API از فایل .env
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_KEY)

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/generate")
def generate():
    prompt = "Write a simple README.md for a sample project."

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    result = response.choices[0].message.content

    return {"response": result}