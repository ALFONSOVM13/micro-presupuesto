from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey, DECIMAL
from database.base import Base

class MSubCategoryDetail(Base):
    __tablename__ = 'm_subcategories_details'

    id = Column(Integer, primary_key=True)
    subcategory_id = Column(Integer, ForeignKey('m_subcategories.id'))
    product_id = Column(Integer, ForeignKey('m_products.id'))
    quantity = Column(DECIMAL)
    unit_value = Column(DECIMAL)
    total_value = Column(DECIMAL)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)