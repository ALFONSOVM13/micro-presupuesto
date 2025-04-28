from modules.FlowModule.models.m_object_states import MObjectState
from modules.FlowModule.repositories.object_state_repository import ObjectStateRepository
from modules.FlowModule.schemas.object_state_schema import ObjectStateCreate, ObjectStateUpdate
from pydantic import ValidationError
from services.base_services import BaseService


class ObjectStateService(BaseService):

    def __init__(self, db):
            self.db = db
            self.repo = ObjectStateRepository(db)
            super().__init__(MObjectState, self.repo)


    def create(self, data: dict) -> MObjectState:
        try:
            object_state = ObjectStateCreate(**data)
        except ValidationError as ve:
            raise ve
        return self.repo.create(object_state.model_dump())

    def update(self, flow_id: int, data: dict) -> MObjectState:
        try:
            validated = ObjectStateUpdate.model_validate(
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