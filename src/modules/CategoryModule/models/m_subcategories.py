from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, DECIMAL
from database.base import Base

class MSubCategory(Base):
    __tablename__ = 'm_subcategories'

    id = Column(Integer, primary_key=True)
    apu = Column(String)
    category_id = Column(Integer, ForeignKey('m_categories.id'))
    name = Column(String)
    total_value = Column(DECIMAL)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)