from fastapi import FastAPI
from app.controller.controllers import router
from fastapi.middleware.cors import CORSMiddleware
from app.utils.config import settings

app = FastAPI(title=settings.PROJECT_NAME)
origins = [
'*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
