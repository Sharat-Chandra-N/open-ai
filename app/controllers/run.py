import os

from dotenv import load_dotenv
from fastapi import APIRouter, Form
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

router = APIRouter(prefix="/runs", tags=["Run"])


@router.post("/create_run")
def create_run(thread_id: str = Form(...), assistant_id: str = Form(...)):
    new_run = client.beta.threads.runs.create(
        thread_id=thread_id, assistant_id=assistant_id
    )
    return new_run


@router.post("/cancel_run")
def cancel_run(thread_id: str = Form(...), run_id: str = Form(...)):
    cancel_run_req = client.beta.threads.runs.cancel(thread_id=thread_id, run_id=run_id)
    return cancel_run_req


@router.post("/get_all_runs")
def get_all_runs(thread_id: str = Form(...)):
    all_runs = client.beta.threads.runs.list(thread_id)
    return all_runs.data
