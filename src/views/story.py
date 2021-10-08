from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/story")
def login_view(request: Request):
    return {"info": "yes"}
