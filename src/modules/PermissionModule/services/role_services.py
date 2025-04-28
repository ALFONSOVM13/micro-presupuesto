from datetime import datetime
from modules.PermissionModule.models.m_role import MRole
from modules.PermissionModule.repositories.role_repository import RoleRepository
from services.base_services import BaseService
class RoleService(BaseService):
    def __init__(self, db):
        self.repository = RoleRepository(db)
        super().__init__(MRole, self.repository)

    def create(self, data):
        role = MRole(
            code=data['code'],
            name=data['name'],
            active=data.get('active', True),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        return self.repository.create(role)

    def update(self, role_id, data):
        return self.repository.update(role_id, data)


    def delete(self, role_id):
        role = self.repository.get_by_id(role_id)
        if not role:
            return False
        self.repository.delete(role)
        return True
