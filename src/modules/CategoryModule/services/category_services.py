from modules.CategoryModule.models.m_categories import MCategory
from datetime import datetime
from modules.CategoryModule.repositories.category_repository import CategoryRepository
from services.base_services import BaseService
class CategoryService(BaseService):
    def __init__(self, db):
        self.repository = CategoryRepository(db)
        super().__init__(MCategory, self.repository)


    def create(self, data):
        category = MCategory(
            name=data['name'],
            region_id=data['region_id'],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        return self.repository.add(category)

    def update(self, category_id, data):
        category = self.repository.get_by_id(category_id)
        if not category:
            return None
        category.name = data.get('name', category.name)
        category.region_id = data.get('region_id', category.region_id)
        category.updated_at = datetime.utcnow()
        self.repository.update()
        return category

    def delete(self, category_id):
        category = self.repository.get_by_id(category_id)
        if not category:
            return False
        self.repository.delete(category)
        return True
