from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.model import Base


class Topic(Base):
    __tablename__ = 'topic'

    en_title = Column(String, index=True)
    id_title = Column(String, index=True)
    verse_topics = relationship("VerseTopic", back_populates="topic")
