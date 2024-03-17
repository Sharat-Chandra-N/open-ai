import os

from dotenv import load_dotenv
from fastapi import APIRouter, Form
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

router = APIRouter(prefix="/assistants", tags=["Assistant"])


@router.post("/create_assistant")
def create_assistant(agent_name: str = Form(...), agent_description: str = Form(...)):
    new_assistant = client.beta.assistants.create(
        name=agent_name, description=agent_description, model="gpt-3.5-turbo-16k"
    )
    return new_assistant


@router.post("/delete_assistant")
def create_assistant(agent_id: str = Form(...)):
    new_assistant = client.beta.assistants.delete(agent_id)
    return new_assistant


@router.get("/get_all_assistants")
def get_all_assistants():
    all_assitants = client.beta.assistants.list()
    return all_assitants.data
