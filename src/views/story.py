from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.base import get_session
from db.dals.story import StoryDAL

router = APIRouter()


@router.get("/story")
async def get_all_stories(session: AsyncSession = Depends(get_session)) -> dict:
    story_dal = StoryDAL(session)
    all_stories = await story_dal.get_all_stories()
    if not all_stories:
        return {"version": "1.0", "startId": 1, "stories": []}
    return all_stories


@router.get("/story/{story_id:int}")
async def get_story(story_id: int, session: AsyncSession = Depends(get_session)):
    story_dal = StoryDAL(session)
    return await story_dal.get_story(story_id)
