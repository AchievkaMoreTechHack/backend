import os

from fastapi import APIRouter
from fastapi.responses import FileResponse

from core.config import BASE_DIR

router = APIRouter()


@router.get("/media/{image_name}")
async def main(image_name: str):
    path = str(BASE_DIR) + f"/media/{image_name}"
    if not os.path.isfile(path):
        return {"error": "No such file"}
    return FileResponse(path)
