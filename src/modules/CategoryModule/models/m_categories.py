from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from database.base import Base

class MCategory(Base):
    __tablename__ = 'm_categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    region_id = Column(Integer, ForeignKey('m_regions.id'))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)