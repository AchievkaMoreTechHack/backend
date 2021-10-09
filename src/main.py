import uvicorn
from fastapi import FastAPI

from core.config import DEBUG
from core.routes import router
from db.base import Base, engine
from services.fixtures import import_fixture


def get_application() -> FastAPI:
    application = FastAPI(debug=DEBUG)

    application.include_router(router)
    return application


app = get_application()


@app.on_event("startup")
async def startup():
    # create db tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    await import_fixture()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
