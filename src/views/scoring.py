from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class ScoringInfo(BaseModel):
    salary: float
    motivation: str
    age: int


@router.post("/scoring/")
async def scoring(info: ScoringInfo):
    motivations = ["save money", "make money"]
    if info.motivation.lower() not in motivations:
        return {"error": f"No such motivation. It should be one of {motivations}"}
