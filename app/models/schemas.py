from pydantic import BaseModel
from typing import List

class Message(BaseModel):
    role:str
    content:str
    
class RequestInput(BaseModel):
    message:List[Message]
    model: str
    temperature: float

class ImageRequestInput(BaseModel):
    prompt: str
    model: str
    quality: str
    size: str
    n: int


class ClaudeRequestInput(BaseModel):
    prompt:str
    model: str
    temperature: float