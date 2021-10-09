from db.base import async_session
from db.models.story import Story


async def import_fixture():
    async with async_session() as session:
        a = Story(story='["asdf", "a"]', prev="asdf1", background="backgroundadf")
        session.add(a)
        await session.commit()
