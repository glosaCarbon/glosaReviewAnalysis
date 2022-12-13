from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers.model import model_router

tags_metadata = [
    {
        "name": "Model Operations",
        "description": "Operations for model",
    }]

app = FastAPI(openapi_tags=tags_metadata)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(model_router, prefix='/model')


@app.get('/')
def index():
    return "Review sentiment analysis"
