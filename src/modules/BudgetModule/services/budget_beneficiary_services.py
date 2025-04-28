from modules.BudgetModule.models.o_budgets_beneficiaries import BudgetBeneficiary
from modules.BudgetModule.schemas.budget_beneficiary_schema import OBudgetBeneficiaryCreate, OBudgetBeneficiaryUpdate
from modules.BudgetModule.repositories.budget_beneficiary_repository import BudgetBeneficiaryRepository
from services.base_services import BaseService
from pydantic import ValidationError

class ParameterValueService(BaseService):
    def __init__(self, db):
        self.db = db
        self.repo = BudgetBeneficiaryRepository(db)
        super().__init__(BudgetBeneficiary, self.repo)
        

    def create(self, data: dict) -> BudgetBeneficiary:
        try:
            budget_beneficiary = OBudgetBeneficiaryCreate(**data)
        except ValidationError as ve:
            raise ve
        return self.repo.create(budget_beneficiary.model_dump())

    def update(self, budget_beneficiary_id: int, data: dict) -> BudgetBeneficiary:
        try:
            validated = OBudgetBeneficiaryUpdate.model_validate(
                data,
                context={'db': self.db, 'id': budget_beneficiary_id}
            ).model_dump(exclude_unset=True)
        except ValidationError as ve:
            raise ve

        return self.repo.update(budget_beneficiary_id, validated)
    
    def delete(self, id):
        value = self.repo.get_by_id(id)
        if not value:
            return False
        self.repo.delete(value)
        return True
