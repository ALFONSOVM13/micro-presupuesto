from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, ForeignKey
from database.base import Base
from database.connection import db

class MParameterValue(Base):
    __tablename__ = 'm_parameters_values'

    id = Column(Integer, primary_key=True)
    parameter_id = Column(Integer, ForeignKey('m_parameters.id'))
    reference = Column(String)
    value = Column(String)
    description = Column(String)
    parent_id = Column(Integer)
    active = Column(Boolean)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)