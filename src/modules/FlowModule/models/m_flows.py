from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from database.base import Base

class MFlow(Base):
    __tablename__ = 'm_flows'


    id = Column(Integer, primary_key=True)
    reference = Column(String, nullable=True)
    flow_name = Column(String, nullable=True)
    active = Column(Boolean, nullable=True, default=True)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True)