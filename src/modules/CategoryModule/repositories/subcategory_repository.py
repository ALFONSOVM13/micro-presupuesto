from modules.CategoryModule.models.m_subcategories import MSubCategory
from repositories.base_repository import BaseRepository
class SubcategoryRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(db, MSubCategory)

    def get_by_id(self, id):
        return self.db.query(MSubCategory).filter(MSubCategory.id == id).first()

    def save(self, subcategory):
        self.db.add(subcategory)
        self.db.commit()
        self.db.refresh(subcategory)
        return subcategory

    def delete(self, subcategory):
        self.db.delete(subcategory)
        self.db.commit()
