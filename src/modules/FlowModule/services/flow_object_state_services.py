from modules.FlowModule.models.m_flow_object_states import MFlowObjectState
from modules.FlowModule.repositories.fos_repository import FOSRepository
from modules.FlowModule.schemas.flow_object_state_schema import FlowObjectStateCreate, FlowObjectStateUpdate
from pydantic import ValidationError
from services.base_services import BaseService


class FlowObjectStateService(BaseService):

    def __init__(self, db):
            self.db = db
            self.repo = FOSRepository(db)
            super().__init__(MFlowObjectState, self.repo)


    def create(self, data: dict) -> MFlowObjectState:
        try:
            flow_in = FlowObjectStateCreate(**data)
        except ValidationError as ve:
            raise ve
        return self.repo.create(flow_in.model_dump())

    def update(self, flow_id: int, data: dict) -> MFlowObjectState:
        try:
            validated = FlowObjectStateUpdate.model_validate(
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