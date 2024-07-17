# schemas.py

from pydantic import BaseModel
from typing import List, Optional


class Verse(BaseModel):
    id: int
    surah_id: int
    verse_number: int
    juz: int
    arabic: str
    latin: str
    id_translation: Optional[str] = None
    en_translation: Optional[str] = None

    class Config:
        orm_mode: True


class Surah(BaseModel):
    id: int
    arabic: str
    latin: str
    number_of_verse: int
    id_translation: Optional[str] = None
    en_translation: Optional[str] = None
    revelation_type: str
    verses: List[Verse] = []

    class Config:
        orm_mode: True


class VerseTopic(BaseModel):
    id: int
    topic_id: int
    verse_id: int

    class Config:
        orm_mode: True


class Topic(BaseModel):
    id: int
    en_title: str
    id_title: str
    topic_verses: List[VerseTopic] = []

    class Config:
        orm_mode: True

