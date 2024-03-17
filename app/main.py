from fastapi import FastAPI

from app.controllers import assistant, query, run, thread

app = FastAPI(title="Open AI API's")

app.include_router(assistant.router)
app.include_router(thread.router)
app.include_router(run.router)
app.include_router(query.router)


@app.get("/", tags=["Root"])
def root():
    return {"OpenAI Application": "Application is Running"}
