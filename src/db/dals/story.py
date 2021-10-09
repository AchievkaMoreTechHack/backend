import json
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from db.models.story import Story
from services.urls import create_url_media, create_url_story


class StoryDAL:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_book(self, name: str, author: str, release_year: int):
        new_book = Story(name=name, author=author, release_year=release_year)
        self.db_session.add(new_book)
        await self.db_session.flush()

    async def get_all_books(self) -> List[Story]:
        q = await self.db_session.execute(select(Story))
        stories = q.scalars().all()
        for story in stories:
            if story.action_data:
                story.action_data = json.loads(story.action_data)
            story.story = json.loads(story.story)
            story.next = create_url_story(story.next)
            story.prev = create_url_story(story.prev)
            story.background = create_url_media(story.background)
            story.character = create_url_media(story.character)
        return stories

    async def get_book(self, id: int) -> Story:
        q = await self.db_session.execute(Story.query.get(id))
        return q
