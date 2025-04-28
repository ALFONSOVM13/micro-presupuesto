from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, ForeignKey
from database.base import Base

class MAction(Base):
    __tablename__ = 'm_actions'

    id = Column(Integer, primary_key=True)
    code = Column(String)
    type_id = Column(Integer, ForeignKey('m_parameters_values.id'), nullable=True)
    name = Column(String)
    active = Column(Boolean)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
