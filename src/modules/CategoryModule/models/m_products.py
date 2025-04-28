from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, ForeignKey, DECIMAL
from database.base import Base

class MProduct(Base):
    __tablename__ = 'm_products'

    id = Column(Integer, primary_key=True)
    reference = Column(String)
    name = Column(String)
    unit_id = Column(Integer, ForeignKey('m_parameters_values.id'))
    value = Column(DECIMAL)
    active = Column(Boolean)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)