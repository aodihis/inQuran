from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from app.database.model import Base


class Verse(Base):
    __tablename__ = 'verse'

    surah_id = Column(Integer, ForeignKey('surah.id'))
    verse_number = Column(Integer)
    juz = Column(Integer)
    arabic = Column(String, index=True)  # This column will store Arabic text
    latin = Column(String, index=True)
    id_translation = Column(String, index=True)
    en_translation = Column(String, index=True)
    surah = relationship("Surah", back_populates="verses")
