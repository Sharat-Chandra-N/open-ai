import os

from dotenv import load_dotenv
from fastapi import APIRouter, Form, HTTPException, status
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

router = APIRouter(prefix="/query", tags=["Query"])


@router.post("/")
def query(thread_id: str = Form(...), run_id: str = Form(...)):
    try:
        run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
        if run.completed_at:
            messages = client.beta.threads.messages.list(thread_id=thread_id)
            last_message = messages.data[0]
            response = last_message.content[0].text.value
            return response
    except Exception as e:
        print(f"An error occurred while retrieving the run: {e}")
