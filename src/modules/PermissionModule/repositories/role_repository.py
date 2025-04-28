from modules.PermissionModule.models.m_role import MRole
from repositories.base_repository import BaseRepository


class RoleRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(db, MRole)

