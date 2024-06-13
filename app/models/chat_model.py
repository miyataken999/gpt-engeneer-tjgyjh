from dataclasses import dataclass

@dataclass
class ChatMessage:
    text: str
    user: str