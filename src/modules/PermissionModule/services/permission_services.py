from datetime import datetime
from modules.PermissionModule.models.c_permissions import CPermission
from modules.PermissionModule.repositories.permission_repository import PermissionRepository
from services.base_services import BaseService


class PermissionService(BaseService):
    def __init__(self, db):
        self.repo = PermissionRepository(db)
        super().__init__(CPermission, self.repo)
        
        
    def create(self, data):
        permission = CPermission(
            associate_to=data['associate_to'],
            associate_id=data['associate_id'],
            action_id=data['action_id'],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        return self.repo.save(permission)

    def update(self, id, data):
        permission = self.get_by_id(id)
        if not permission:
            return None
        permission.associate_to = data.get('associate_to', permission.associate_to)
        permission.associate_id = data.get('associate_id', permission.associate_id)
        permission.action_id = data.get('action_id', permission.action_id)
        permission.updated_at = datetime.utcnow()
        return self.repo.save(permission)

    def delete(self, id):
        permission = self.get_by_id(id)
        if not permission:
            return False
        self.repo.delete(permission)
        return True
