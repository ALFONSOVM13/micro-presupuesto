from sqlalchemy.orm import Session
from modules.BudgetModule.models.o_budgets import OBudget
from modules.BudgetModule.schemas.budget_schema import OBudgetCreate, OBudgetUpdate
from repositories.base_repository import BaseRepository
class OBudgetRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db, OBudget)

    def get_by_id(self, budget_id: int):
        return self.db.query(OBudget).filter(OBudget.id == budget_id).first()

    def create(self, data: OBudgetCreate):
        new_budget = OBudget(**data.dict())
        self.db.add(new_budget)
        self.db.commit()
        self.db.refresh(new_budget)
        return new_budget

    def update(self, budget_id: int, data: OBudgetUpdate):
        budget = self.get_by_id(budget_id)
        if not budget:
            return None
        for key, value in data.dict().items():
            setattr(budget, key, value)
        self.db.commit()
        self.db.refresh(budget)
        return budget

    def delete(self, budget_id: int):
        budget = self.get_by_id(budget_id)
        if not budget:
            return None
        self.db.delete(budget)
        self.db.commit()
        return budget
