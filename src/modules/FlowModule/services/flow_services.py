from modules.FlowModule.models.m_flows import MFlow
from modules.FlowModule.repositories.flow_repository import FlowRepository
from modules.FlowModule.schemas.flow_schema import FlowCreate, FlowUpdate
from pydantic import ValidationError
from services.base_services import BaseService


class FlowService(BaseService):

    def __init__(self, db):
            self.db = db
            self.repo = FlowRepository(db)
            super().__init__(MFlow, self.repo)


    def create(self, data: dict) -> MFlow:
        try:
            flow_in = FlowCreate(**data)
        except ValidationError as ve:
            raise ve
        return self.repo.create(flow_in.model_dump())

    def update(self, flow_id: int, data: dict) -> MFlow:
        try:
            validated = FlowUpdate.model_validate(
                data,
                context={'db': self.db, 'id': flow_id}
            ).model_dump(exclude_unset=True)
        except ValidationError as ve:
            raise ve

        return self.repo.update(flow_id, validated)
    
    def delete(self, action_id):
        action = self.repo.get_by_id(action_id)
        if not action:
            return False
        self.repo.delete(action)
        return True