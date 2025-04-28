from modules.ParameterModule.models.m_parameters import MParameter
from modules.ParameterModule.schemas.parameter_schema import MParameterCreate, MParameterUpdate
from modules.ParameterModule.repositories.parameter_repository import ParameterRepository
from services.base_services import BaseService
from pydantic import ValidationError
class ParameterService(BaseService):
    def __init__(self, db):
        self.db = db
        self.repo = ParameterRepository(db)
        super().__init__(MParameter, self.repo)
        
    def create(self, data: dict) -> MParameter:
        try:
            pv_in = MParameterCreate(**data)
        except ValidationError as ve:
            raise ve
        return self.repo.create(pv_in.model_dump())

    def update(self, pv_id: int, data: dict) -> MParameter:
        try:
            validated = MParameterUpdate.model_validate(
                data,
                context={'db': self.db, 'id': pv_id}
            ).model_dump(exclude_unset=True)
        except ValidationError as ve:
            raise ve

        return self.repo.update(pv_id, validated)
    
    def delete(self, parameter_id):
        parameter = self.get_by_id(parameter_id)
        if not parameter:
            return False
        self.repo.delete(parameter)
        return True
