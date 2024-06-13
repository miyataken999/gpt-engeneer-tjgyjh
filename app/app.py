from fastapi import FastAPI
from views.chat_view import chat_router

app = FastAPI()

app.include_router(chat_router)