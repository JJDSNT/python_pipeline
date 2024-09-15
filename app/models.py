from sqlalchemy import Column, Integer, String, Float
from .database import Base


class RawData(Base):
    __tablename__ = 'raw_data'
    id = Column(Integer, primary_key=True, index=True)
    field1 = Column(String)
    field2 = Column(Float)
    # Outros campos...


class EnrichedData(Base):
    __tablename__ = 'enriched_data'
    id = Column(Integer, primary_key=True, index=True)
    raw_data_id = Column(Integer)
    enriched_field = Column(String)
    # Outros campos...
