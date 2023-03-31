from fastapi import FastAPI, Depends
from dotenv import load_dotenv
from src.dependency import openai_dependency as openai
from fastapi.responses import JSONResponse

# Load the environment variables from the .env file
load_dotenv()
app = FastAPI()


@app.get("/")
async def root():
  return {"message": "Hello World"}


@app.get("/health")
async def health():
  return {"status": "ok"}



@app.post("/chat")
async def chat(*, openai=Depends(openai), message: str) -> str:

  try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
          {
            "role": "user",
            "content": message
          }
        ]
    )
    token_used = response['usage']['total_tokens']
    print(f"Token used: {token_used}")
    return response['choices'][0]['message']['content']
  except Exception as e:
    print(e)
    return "Sorry, I don't understand your question"

