from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database.model import Base


class VerseTopic(Base):
    __tablename__ = 'verse_topic'

    topic_id = Column(Integer, ForeignKey('topic.id'))
    verse_id = Column(Integer, ForeignKey('verse.id'))
    topic = relationship("Topic", back_populates="verse_topics")
    verses = relationship("Verse", back_populates="topic")
