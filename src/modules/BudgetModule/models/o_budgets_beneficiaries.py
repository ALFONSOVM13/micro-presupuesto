from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey
from database.base import Base

class BudgetBeneficiary(Base):
    __tablename__ = 'o_budgets_beneficiaries'

    id = Column(Integer, primary_key=True)
    beneficiary_id = Column(Integer)
    budget_id = Column(Integer, ForeignKey('o_budgets.id'))
    status_id = Column(Integer, ForeignKey('m_object_states.id'))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)