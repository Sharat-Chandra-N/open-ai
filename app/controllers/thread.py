import os

from dotenv import load_dotenv
from fastapi import APIRouter, Form, HTTPException, status
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

router = APIRouter(prefix="/thread", tags=["Thread"])


@router.post("/create_thread")
def create_thread():
    new_thread = client.beta.threads.create()
    return new_thread


@router.post("/get_thread")
def get_thread(thread_id: str = Form(...)):
    thread_data = client.beta.threads.retrieve(thread_id)
    if thread_data is None:
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Thread Not Found")
    return thread_data


@router.post("/delete_thread")
def delete_thread(thread_id: str = Form(...)):
    thread = client.beta.threads.delete(thread_id)
    if thread is None:
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Thread Not Found")
    return thread
