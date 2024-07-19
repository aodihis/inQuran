from functools import lru_cache
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from .config import Config
import app.api.schemas as schemas
import app.api.service as service
from app.database.session import get_db_session
from sqlalchemy.ext.asyncio import (
    AsyncSession,
)
import strawberry
from app.api.gqlschemas import Query
from strawberry.fastapi import GraphQLRouter


async def get_context(db=Depends(get_db_session)):
    return {
        "db": db,
    }


schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema, context_getter=get_context)

app = FastAPI()


@lru_cache
def get_configs():
    return Config()


app.include_router(graphql_app, prefix="/graphql")


@app.get("/verse/{surah_number}/{verse_number}", response_model=schemas.Verse)
async def read_users(surah_number: int, verse_number: int, db: AsyncSession = Depends(get_db_session)):
    verse = await service.get_verse(db=db, surah_number=surah_number, verse_number=verse_number)
    return verse


@app.get("/surah/{surah_number}", response_model=schemas.Surah)
async def read_surah(surah_number: int, db: AsyncSession = Depends(get_db_session)):
    surah = await service.get_surah(db, surah_number)
    return surah


@app.get("/topic", response_model=list[schemas.Topic])
async def read_topic(db: AsyncSession = Depends(get_db_session)):
    topics = await service.get_list_topic(db)
    return topics


@app.get("/topic/{topic_id}", response_model=schemas.VerseTopic)
async def read_verse_topic(topic_id: int, db: AsyncSession = Depends(get_db_session)):
    verse = await service.get_verse_by_topic(db, topic_id)
    return verse
