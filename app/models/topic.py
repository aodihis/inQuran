from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.database.model import Base

verse_topic = Table('verse_topic', Base.metadata,
                    Column('topic_id', Integer, ForeignKey('topic.id'), primary_key=False),
                    Column('verse_id', Integer, ForeignKey('verse.id'), primary_key=False)
                    )


class Topic(Base):
    __tablename__ = 'topic'

    en_title = Column(String, index=True)
    id_title = Column(String, index=True)
    verses = relationship('Verse', secondary=verse_topic, backref='topic')
