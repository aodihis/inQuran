from sqlalchemy import select

from . import schemas
from app.models.verse import Verse
from sqlalchemy.orm import Session, selectinload
from app.models.surah import Surah
from app.models.topic import Topic
# from app.models.versetopic import VerseTopic
from sqlalchemy.ext.asyncio import (
    AsyncSession,
)


async def get_verse(db: AsyncSession, surah_number: int, verse_number: int):
    statement = (select(Verse)
                 .where(Verse.verse_number == verse_number)
                 .where(Verse.surah_id == surah_number))
    verse: Verse = (await db.execute(statement)).scalar()
    return verse


async def get_surah(db: AsyncSession, surah_number: int) -> Surah:
    statement = (select(Surah)
                 .where(Surah.id == surah_number))
    surah: Surah = (await db.execute(statement)).scalar()
    return surah


async def get_list_topic(db: AsyncSession):
    statement = (select(Topic))
    topics: [Topic] = (await db.execute(statement)).scalars().all()
    return topics


async def get_verse_by_topic(db: AsyncSession, topic_id: int):
    statement = (select(Topic)
                 .where(Topic.id == topic_id).options(selectinload(Topic.verses)))
    verse_topic: Topic = (await db.execute(statement)).scalar()
    return verse_topic
