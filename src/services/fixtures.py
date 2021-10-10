import json

from db.base import async_session
from db.models.story import Story
from services.data.fixture import fixtures
from services.urls import create_url_story


async def import_fixture():
    async with async_session() as session:
        fixture_len = len(fixtures)
        for id, story_dict in enumerate(fixtures):
            id = id + 1
            next = str(id + 1)
            prev_loc = str(id - 1)
            if "next" in story_dict.keys():
                next = story_dict.pop("next")
            if "prev" in story_dict.keys():
                prev_loc = story_dict.pop("prev")
            if id == 1:
                prev_loc = None
            if id == str(fixture_len):
                next = None
            story = Story(id=id, next=next, prev=prev_loc, **story_dict)
            if not story.story_female or not story.story_male or not story.background:
                raise Exception("no required fields")
            if story.action_type == "button":
                new_list_male = json.loads(story.action_data_male)
                for index, value in enumerate(new_list_male):
                    if index % 2 == 1:
                        new_list_male[index] = create_url_story(value)
                story.action_data_male = json.dumps(new_list_male)

                new_list_female = json.loads(story.action_data_female)
                for index, value in enumerate(new_list_female):
                    if index % 2 == 1:
                        new_list_female[index] = create_url_story(value)
                story.action_data_female = json.dumps(new_list_female)
            session.add(story)
        await session.commit()
