from pydantic import BaseModel


class RequestInput(BaseModel):
    prompt: str
      
class ImageRequestInput(BaseModel):
    prompt: str
    model: str
    quality:str
    size:str
    n:int

    
   
