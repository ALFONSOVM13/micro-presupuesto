from modules.PermissionModule.models.m_module import MModule
from repositories.base_repository import BaseRepository
class ModuleRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(db, MModule)

    def get_by_id(self, module_id):
        return self.db.query(MModule).filter(MModule.id == module_id).first()

    def save(self, module):
        self.db.add(module)
        self.db.commit()
        self.db.refresh(module)
        return module

    def delete(self, module):
        self.db.delete(module)
        self.db.commit()
