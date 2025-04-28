from sqlalchemy import Column, Integer, String, Date, TIMESTAMP, ForeignKey, DECIMAL
from database.base import Base

class OBudget(Base):
    __tablename__ = 'o_budgets'

    id = Column(Integer, primary_key=True)
    code = Column(String)
    contractor_id = Column(Integer)
    contract_id = Column(Integer)
    department_id = Column(Integer)
    municipality_id = Column(Integer)
    village = Column(String)
    resolution_id = Column(Integer)
    improvement_type_id = Column(Integer, ForeignKey('m_parameters_values.id'))
    specific_improvement_id = Column(Integer, ForeignKey('m_parameters_values.id'))
    valid_year = Column(Integer)
    minimum_salary_id = Column(Integer, ForeignKey('m_parameters_values.id'))
    presentation_date = Column(Date)
    scheme_type_id = Column(Integer, ForeignKey('m_parameters_values.id'))
    legal_minimum_wages = Column(Integer)
    subtotal_direct_costs = Column(DECIMAL)
    subtotal_indirect_costs = Column(DECIMAL)
    total_diagnosis = Column(DECIMAL)
    total_budget = Column(DECIMAL)
    status_id = Column(Integer, ForeignKey('m_object_states.id'))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)