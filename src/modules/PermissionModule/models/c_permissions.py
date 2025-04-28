from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from database.base import Base

class CPermission(Base):
    __tablename__ = 'c_permissions'

    id = Column(Integer, primary_key=True)
    associate_to = Column(String)
    associate_id = Column(Integer)
    action_id = Column(Integer, ForeignKey('c_modules_actions.id'))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)