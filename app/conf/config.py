import os

def custom_openapi(app):

    original_openapi = app.openapi

    def openapi():
        if app.openapi_schema:
            return app.openapi_schema
        
        openapi_schema = original_openapi().copy()

        server_url = os.getenv(
            "BASE_URL",
            "http://localhost:8000"
        )

        openapi_schema["servers"] = [{
            "url": server_url,
            "description":"Production server" if "run.app" in server_url else "Local server"
        }]

        app.openapi_schema = openapi_schema
        return app.openapi_schema

    return openapi