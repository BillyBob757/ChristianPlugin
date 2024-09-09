import openai
import os
from fastapi import FastAPI
from pydantic import BaseModel

# Initialize OpenAI client using the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Define the data model for user input
class UserInput(BaseModel):
    message: str

@app.post("/chat/")
def christian_support(input: UserInput):
    message = input.message
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Christian counselor providing Bible-based guidance."},
                {"role": "user", "content": message}
            ],
            max_tokens=300
        )
        assistant_response = response['choices'][0]['message']['content'].strip()
        return {"response": assistant_response}
    except Exception as e:
        return {"error": str(e)}
