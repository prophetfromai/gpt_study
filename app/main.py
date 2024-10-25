from fastapi import FastAPI
from fastapi.responses import RedirectResponse, PlainTextResponse
from app.routes import router
import os

server_url = os.getenv('BASE_URL', 'https://localhost:8080')

app = FastAPI(
    title='GPT Notes',
    version='1.0.0',
    servers=[{'url':'serverurl','description':'Production server' if 'run.app' in server_url else 'Local server'}]
)

app.include_router(router)

@app.get('/', include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url='docs/')

@app.get('/privacy', response_class=PlainTextResponse)
async def get_privacy_policy():
    return """
    Privacy Policy

    This is the privacy policy for our application. We respect your privacy and ensure that your data is protected. 
    We do not share personal information with third parties, except as necessary to provide our services.
    """