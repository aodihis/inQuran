from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database.model import Base


class Surah(Base):
    __tablename__ = 'surah'

    arabic = Column(String, index=True)
    latin = Column(String, index=True)
    number_of_verse = Column(Integer)
    id_translation = Column(String, index=True)
    en_translation = Column(String, index=True)
    revelation_type = Column(String)
    verses = relationship("Verse", back_populates="surah", lazy='joined')
