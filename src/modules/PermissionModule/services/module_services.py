from datetime import datetime
from modules.PermissionModule.models.m_module import MModule
from modules.PermissionModule.repositories.module_repository import ModuleRepository
from services.base_services import BaseService

class ModuleService(BaseService):
    def __init__(self, db):
        self.db = db
        self.repo = ModuleRepository(db)
        super().__init__(MModule, self.repo)


    def create(self, data):
        module = MModule(
            level=data.get('level'),
            name=data.get('name'),
            path=data.get('path'),
            parent_id=data.get('parent_id'),
            active=data.get('active', True),
            position=data.get('position'),
            icon=data.get('icon'),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        return self.repo.save(module)

    def update(self, module_id, data):
        module = self.get_by_id(module_id)
        if not module:
            return None

        module.level = data.get('level', module.level)
        module.name = data.get('name', module.name)
        module.path = data.get('path', module.path)
        module.parent_id = data.get('parent_id', module.parent_id)
        module.active = data.get('active', module.active)
        module.position = data.get('position', module.position)
        module.icon = data.get('icon', module.icon)
        module.updated_at = datetime.utcnow()

        return self.repo.save(module)

    def delete(self, module_id):
        module = self.get_by_id(module_id)
        if not module:
            return False
        self.repo.delete(module)
        return True
