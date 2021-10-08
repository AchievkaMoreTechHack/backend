import uvicorn
from fastapi import FastAPI

from core.routes import router
from core.config import DEBUG


def get_application() -> FastAPI:
    application = FastAPI(debug=DEBUG)

    application.include_router(router)
    return application


app = get_application()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
