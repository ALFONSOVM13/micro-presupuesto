from sqlalchemy.orm import Session
from modules.BudgetModule.models.o_budgets_beneficiaries import BudgetBeneficiary
from modules.BudgetModule.schemas.budget_beneficiary_schema import  OBudgetBeneficiaryCreate, OBudgetBeneficiaryUpdate
from repositories.base_repository import BaseRepository

class  BudgetBeneficiaryRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db,  BudgetBeneficiary)

    def get_by_id(self, budget_beneficiary_id: int):
        return self.db.query( BudgetBeneficiary).filter(BudgetBeneficiary.id == budget_beneficiary_id).first()

    def create(self, data:  OBudgetBeneficiaryCreate):
        new_budget_beneficiary =  BudgetBeneficiary(**data.dict())
        self.db.add(new_budget_beneficiary)
        self.db.commit()
        self.db.refresh(new_budget_beneficiary)
        return new_budget_beneficiary

    def update(self, budget_beneficiary_id: int, data:  OBudgetBeneficiaryUpdate):
        budget_beneficiary = self.get_by_id(budget_beneficiary_id)
        if not budget_beneficiary:
            return None
        for key, value in data.dict().items():
            setattr(budget_beneficiary, key, value)
        self.db.commit()
        self.db.refresh(budget_beneficiary)
        return budget_beneficiary

    def delete(self, budget_beneficiary_id: int):
        budget_beneficiary = self.get_by_id(budget_beneficiary_id)
        if not budget_beneficiary:
            return None
        self.db.delete(budget_beneficiary)
        self.db.commit()
        return budget_beneficiary
