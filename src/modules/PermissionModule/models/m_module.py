from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from database.base import Base

class MModule(Base):
    __tablename__ = 'm_modules'

    id = Column(Integer, primary_key=True)
    level = Column(Integer)
    name = Column(String)
    path = Column(String)
    parent_id = Column(Integer)
    active = Column(Boolean)
    position = Column(Integer)
    icon = Column(String)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
