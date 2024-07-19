from typing import List, Optional

from .schemas import Verse, Surah
import strawberry
import app.api.service as service
from app.models.verse import Verse as VerseModel
from app.models.surah import Surah as SurahModel
from app.models.topic import Topic as TopicModel


@strawberry.type
class VerseType:
    id: strawberry.ID
    surah_id: int
    verse_number: int
    juz: int
    arabic: str
    latin: str
    id_translation: str
    en_translation: str

    @classmethod
    def marshal(cls, model: VerseModel) -> "VerseType":
        return cls(
            id=model.id,
            surah_id=model.surah_id,
            verse_number=model.verse_number,
            juz=model.juz,
            arabic=model.arabic,
            latin=model.latin,
            id_translation=model.id_translation,
            en_translation=model.en_translation
        )


@strawberry.type
class SurahType:
    id: strawberry.ID
    arabic: str
    latin: str
    number_of_verse: int
    id_translation: str
    en_translation: str
    revelation_type: str
    verses: List[VerseType]

    @classmethod
    def marshal(cls, model: SurahModel) -> "SurahType":
        return cls(
            id=model.id,
            arabic=model.arabic,
            latin=model.latin,
            number_of_verse=model.number_of_verse,
            id_translation=model.id_translation,
            en_translation=model.en_translation,
            revelation_type=model.revelation_type,
            verses=model.verses,
        )


@strawberry.type
class TopicType:
    id: strawberry.ID
    en_title: str
    id_title: str

    @classmethod
    def marshal(cls, model: TopicModel) -> "TopicType":
        return cls(
            id=model.id,
            en_title=model.en_title,
            id_title=model.id_title,
        )


@strawberry.type
class VerseTopicType(TopicType):
    verses: Optional[List[VerseType]]

    @classmethod
    def marshal(cls, model: TopicModel) -> "VerseTopicType":
        return cls(
            id=model.id,
            en_title=model.en_title,
            id_title=model.id_title,
            verses=model.verses,
        )


@strawberry.type
class Query:
    @strawberry.field
    async def surah(self, surah_number: int, info: strawberry.Info) -> SurahType:
        surah = await service.get_surah(info.context['db'], surah_number)
        return SurahType.marshal(surah)

    @strawberry.field
    async def verse(self, surah_number: int, verse_number: int, info: strawberry.Info) -> VerseType:
        verse = await service.get_verse(info.context['db'], surah_number, verse_number)
        return VerseType.marshal(verse)

    @strawberry.field
    async def topics(self, info: strawberry.Info) -> list[TopicType]:
        topics = await service.get_list_topic(info.context['db'])
        return [TopicType.marshal(topic) for topic in topics]

    @strawberry.field
    async def verse_topic(self, topic_id: int, info: strawberry.Info) -> VerseTopicType:
        verse_topic = await service.get_verse_by_topic(info.context['db'], topic_id)
        return VerseTopicType.marshal(verse_topic)
