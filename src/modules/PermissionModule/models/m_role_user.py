from sqlalchemy import Column, Integer, Boolean, TIMESTAMP, ForeignKey
from database.base import Base

class MRoleUser(Base):
    __tablename__ = 'm_roles_users'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    role_id = Column(Integer, ForeignKey('m_roles.id'))
    active = Column(Boolean)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
