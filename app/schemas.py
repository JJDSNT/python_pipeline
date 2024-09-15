from pydantic import BaseModel

class RawDataSchema(BaseModel):
    field1: str
    field2: float
    # Outros campos...

class EnrichedDataSchema(BaseModel):
    raw_data_id: int
    enriched_field: str
    # Outros campos...

    class Config:
        orm_mode = True
