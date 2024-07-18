from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database.model import Base
from sqlalchemy.ext.associationproxy import association_proxy


# class VerseTopic(Base):
#     __tablename__ = 'verse_topic'
#
#     topic_id = Column(Integer, ForeignKey('topic.id'))
#     verse_id = Column(Integer, ForeignKey('verse.id'))
#     topic = relationship("Topic", back_populates="verse_topics", uselist=False)
#     en_topic = association_proxy('topic', 'en_title')
#     id_topic = association_proxy('topic', 'id_title')
#     verse = relationship("Verse", back_populates="topic")
