from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from database.base import Base

class MObjectState(Base):
    __tablename__ = 'm_object_states'


    id = Column(Integer, primary_key=True)
    reference = Column(String, nullable=True)
    name = Column(String, nullable=True)
    active = Column(Boolean, nullable=True)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True)