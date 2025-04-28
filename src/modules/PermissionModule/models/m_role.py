from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from database.base import Base

class MRole(Base):
    __tablename__ = 'm_roles'

    id = Column(Integer, primary_key=True)
    code = Column(String)
    name = Column(String)
    old_id = Column(Integer)
    active = Column(Boolean)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
