from modules.CategoryModule.models.m_categories import MCategory
from repositories.base_repository import BaseRepository
class CategoryRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(db, MCategory)


    def get_by_id(self, category_id):
        return self.db.query(MCategory).filter(MCategory.id == category_id).first()

    def add(self, category):
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)
        return category

    def update(self):
        self.db.commit()

    def delete(self, category):
        self.db.delete(category)
        self.db.commit()
