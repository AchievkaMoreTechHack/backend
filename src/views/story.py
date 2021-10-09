from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.base import get_session
from db.dals.story import StoryDAL
from db.models.story import Story

router = APIRouter()


@router.get("/story")
async def get_all_stories(session: AsyncSession = Depends(get_session)) -> List[Story]:
    story_dal = StoryDAL(session)
    return await story_dal.get_all_books()


@router.get("/story/{story_id}")
async def update_book(story_id: int, session: AsyncSession = Depends(get_session)):
    story_dal = StoryDAL(session)
    return await story_dal.get_book(story_id)
