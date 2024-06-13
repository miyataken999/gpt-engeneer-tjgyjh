from fastapi import APIRouter, Response
from gradio import Interface, Textbox, Button
from gradio.inputs import Textbox as GradioTextbox
from gradio.outputs import Textbox as GradioTextboxOutput
from models.chat_model import ChatMessage

router = APIRouter()

interface = Interface(
    fn=lambda x: {"message": x, "user": "AI"},
    inputs=GradioTextbox(lines=5, placeholder="Type your message..."),
    outputs=GradioTextboxOutput(),
    title="Chat Interface",
    description="A simple chat interface"
)

@router.get("/chat")
async def get_chat_interface():
    return interface.launch()

@router.post("/chat")
async def post_chat_message(message: str):
    chat_message = ChatMessage(text=message, user="User")
    response = interface.process([message])
    return {"message": response["message"], "user": "AI"}