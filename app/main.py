from fastapi import FastAPI
from fastapi.responses import RedirectResponse, PlainTextResponse
from app.routes.gpt import router
from app.conf.config import custom_openapi


app = FastAPI(
    title='GPT Notes',
    version='1.0.0'
)


app.include_router(router)

app.openapi = custom_openapi(app)

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