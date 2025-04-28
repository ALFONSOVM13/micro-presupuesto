from modules.ParameterModule.models.m_parameters_values import MParameterValue
from modules.ParameterModule.schemas.parameter_value_schema import MParameterValueCreate, MParameterValueUpdate
from modules.ParameterModule.repositories.pv_repository import ParameterValueRepository
from services.base_services import BaseService
from pydantic import ValidationError

class ParameterValueService(BaseService):
    def __init__(self, db):
        self.db = db
        self.repo = ParameterValueRepository(db)
        super().__init__(MParameterValue, self.repo)
        

    def create(self, data: dict) -> MParameterValue:
        try:
            pv_in = MParameterValueCreate(**data)
        except ValidationError as ve:
            raise ve
        return self.repo.create(pv_in.model_dump())

    def update(self, pv_id: int, data: dict) -> MParameterValue:
        try:
            validated = MParameterValueUpdate.model_validate(
                data,
                context={'db': self.db, 'id': pv_id}
            ).model_dump(exclude_unset=True)
        except ValidationError as ve:
            raise ve

        return self.repo.update(pv_id, validated)
    
    def delete(self, id):
        value = self.repo.get_by_id(id)
        if not value:
            return False
        self.repo.delete(value)
        return True
