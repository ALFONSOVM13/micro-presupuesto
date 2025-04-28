from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from database.base import Base

class MParameter(Base):
    __tablename__ = 'm_parameters'

    id = Column(Integer, primary_key=True)
    reference = Column(String)
    value = Column(String)
    active = Column(Boolean)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)