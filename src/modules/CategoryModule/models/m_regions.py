from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from database.base import Base

class MRegion(Base):
    __tablename__ = 'm_regions'

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, index=True)
    name = Column(String)
    active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
