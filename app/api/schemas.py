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


class Topic(BaseModel):
    id: int
    en_title: str
    id_title: str

    class Config:
        orm_mode: True


class VerseTopic(Topic):
    id: int
    verses: List[Verse] = []

    class Config:
        orm_mode: True
