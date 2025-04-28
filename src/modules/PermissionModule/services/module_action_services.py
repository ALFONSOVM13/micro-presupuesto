from datetime import datetime
from modules.PermissionModule.models.c_module_actions import CModuleAction
from modules.PermissionModule.repositories.module_action_repository import ModuleActionRepository
from services.base_services import BaseService

class ModuleActionService(BaseService):
    def __init__(self, db):
        self.db = db
        self.repo = ModuleActionRepository(db)
        super().__init__(CModuleAction, self.repo)

    def create(self, data):
        module_action = CModuleAction(
            module_id=data['module_id'],
            action_id=data['action_id'],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        return self.repo.create(module_action)

    def update(self, id, data):
        module_action = self.get_by_id(id)
        if not module_action:
            return None

        module_action.module_id = data.get('module_id', module_action.module_id)
        module_action.action_id = data.get('action_id', module_action.action_id)
        module_action.updated_at = datetime.utcnow()

        return self.repo.update(module_action)

    def delete(self, id):
        module_action = self.get_by_id(id)
        if not module_action:
            return False
        self.repo.delete(module_action)
        return True
