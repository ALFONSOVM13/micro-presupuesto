from datetime import datetime
from modules.CategoryModule.models.m_subcategories import MSubCategory
from modules.CategoryModule.repositories.subcategory_repository import SubcategoryRepository
from services.base_services import BaseService
class SubcategoryService(BaseService):
    def __init__(self, db):
        self.repo = SubcategoryRepository(db)
        super().__init__(MSubCategory, self.repo)
        

    def create(self, data):
        subcategory = MSubCategory(
            apu=data['apu'],
            category_id=data['category_id'],
            name=data['name'],
            total_value=data['total_value'],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        return self.repo.save(subcategory)

    def update(self, id, data):
        subcategory = self.repo.get_by_id(id)
        if not subcategory:
            return None
        subcategory.apu = data.get('apu', subcategory.apu)
        subcategory.category_id = data.get('category_id', subcategory.category_id)
        subcategory.name = data.get('name', subcategory.name)
        subcategory.total_value = data.get('total_value', subcategory.total_value)
        subcategory.updated_at = datetime.utcnow()
        return self.repo.save(subcategory)

    def delete(self, id):
        subcategory = self.repo.get_by_id(id)
        if not subcategory:
            return False
        self.repo.delete(subcategory)
        return True
