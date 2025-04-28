from modules.PermissionModule.models.m_actions import MAction
from services.base_services import BaseService
from datetime import datetime
from modules.PermissionModule.repositories.action_repository import ActionRepository
from modules.PermissionModule.schemas.action_schema import (
    MActionCreateValidator,
    MActionUpdateValidator
)
class ActionService(BaseService):
    def __init__(self, db):
        self.db = db
        self.repo = ActionRepository(db)
        super().__init__(MAction, self.repo)


    def create(self, data: dict) -> MAction:
        validated = MActionCreateValidator(__db__=self.db, **data).dict(exclude={"__db__"})
        action = MAction(**validated)
        return self.repo.create(action)

    def update(self, action_id: int, data: dict) -> MAction:
        validated = MActionUpdateValidator(
            __db__=self.db, __id__=action_id, **data
        ).dict(exclude={"__db__", "__id__"}, exclude_unset=True)
        return self.repo.update(action_id, validated)
    
    
    def delete(self, action_id):
        action = self.repo.get_by_id(action_id)
        if not action:
            return False
        self.repo.delete(action)
        return True
