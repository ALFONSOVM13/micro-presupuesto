from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey
from database.base import Base

class CModuleAction(Base):
    __tablename__ = 'c_modules_actions'

    id = Column(Integer, primary_key=True)
    module_id = Column(Integer, ForeignKey('m_modules.id'))
    action_id = Column(Integer, ForeignKey('m_actions.id'))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
