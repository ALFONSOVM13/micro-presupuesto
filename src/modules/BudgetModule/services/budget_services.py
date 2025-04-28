from services.base_services import BaseService
from sqlalchemy.orm import Session
from modules.BudgetModule.schemas.budget_schema import OBudgetCreate, OBudgetUpdate
from modules.BudgetModule.repositories.budget_repository import OBudgetRepository
from modules.BudgetModule.models.o_budgets import OBudget


class OBudgetService(BaseService):
    def __init__(self, db: Session):
        self.repository = OBudgetRepository(db)
        super().__init__(OBudget, self.repository)


    def create_budget(self, data: OBudgetCreate):
        return self.repository.create(data)

    def update_budget(self, budget_id: int, data: OBudgetUpdate):
        return self.repository.update(budget_id, data)

    def delete_budget(self, budget_id: int):
        return self.repository.delete(budget_id)
