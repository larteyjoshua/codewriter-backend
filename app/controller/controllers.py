from fastapi import APIRouter
from app.services import code_writer
from app.models import schemas
router = APIRouter(prefix="/v1")


@router.get("/models",)
async def list_models():
    return await code_writer.model_listing()

@router.post("/generate-code")
async def generate_code(parameter: schemas.RequestInput):
    return await code_writer.code_writing(parameter)

@router.post("/generate-image")
async def generate_image(parameter: schemas.ImageRequestInput):
    return await code_writer.image_generating(parameter)

@router.get("/hello")
async def hello_world():
    return {"data": "Hello World From Code Writer"}
