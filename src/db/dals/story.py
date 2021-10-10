import json

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from db.models.story import Story
from services.urls import create_url_media, create_url_story


def fill_story(story):
    if story.action_data_male:
        story.action_data_male = json.loads(story.action_data_male)
        story.action_data_female = json.loads(story.action_data_female)
    story.story_male = json.loads(story.story_male)
    story.story_female = json.loads(story.story_female)
    story.next = create_url_story(story.next)
    story.prev = create_url_story(story.prev)
    story.background = create_url_media(story.background)
    story.character = create_url_media(story.character)
    return story


class StoryDAL:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_all_stories(self) -> dict:
        q = await self.db_session.execute(select(Story))
        stories = q.scalars().all()
        for index, story in enumerate(stories):
            stories[index] = fill_story(story)
        return_data = {"version": "1.0", "startId": 1, "stories": stories}
        return return_data

    async def get_story(self, id: int) -> dict:
        q = await self.db_session.execute(select(Story))
        stories = q.scalars().all()
        for story in stories:
            if story.id == id:
                return fill_story(story)
        return {"error": "No such story"}
