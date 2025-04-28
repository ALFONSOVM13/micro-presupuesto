from modules.PermissionModule.models.c_permissions import CPermission
from repositories.base_repository import BaseRepository
class PermissionRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(db, CPermission)


    def get_by_id(self, id):
        return self.db.query(CPermission).filter(CPermission.id == id).first()

    def save(self, permission):
        self.db.add(permission)
        self.db.commit()
        self.db.refresh(permission)
        return permission

    def delete(self, permission):
        self.db.delete(permission)
        self.db.commit()
