from fastapi import FastAPI
from app.routes.gpt import router
from app.conf.config import custom_openapi


app = FastAPI(
    title='GPT Notes',
    version='1.0.0'
)


app.include_router(router)

app.openapi = custom_openapi(app)