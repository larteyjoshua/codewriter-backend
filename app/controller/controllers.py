from fastapi import APIRouter, Depends
from app.services import code_writer
from app.models import schemas
from app.security.security import get_session_code
router = APIRouter(prefix="/v1")


@router.get("/models")
async def list_models():
    return await code_writer.model_listing()

@router.post("/generate-code")
async def generate_code(parameter: schemas.RequestInput,  x_session_code: str = Depends(get_session_code)):
    return await code_writer.code_writing(parameter)

@router.post("/generate-image")
async def generate_image(parameter: schemas.ImageRequestInput,  x_session_code: str = Depends(get_session_code)):
    return await code_writer.image_generating(parameter)

@router.get("/hello")
async def hello_world():
    return {"data": "Hello World From Code Writer"}
