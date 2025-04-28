from datetime import datetime
from modules.CategoryModule.models.m_products import MProduct
from modules.CategoryModule.repositories.product_repository import ProductRepository
from services.base_services import BaseService 


class ProductService(BaseService):
    def __init__(self, db):
        self.repo = ProductRepository(db)
        super().__init__(MProduct, self.repo)


    def create(self, data):
        product = MProduct(
            reference=data['reference'],
            name=data['name'],
            unit_id=data['unit_id'],
            value=data['value'],
            active=data.get('active', True),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        return self.repo.save(product)

    def update(self, id, data):
        product = self.repo.get_by_id(id)
        if not product:
            return None
        product.reference = data.get('reference', product.reference)
        product.name = data.get('name', product.name)
        product.unit_id = data.get('unit_id', product.unit_id)
        product.value = data.get('value', product.value)
        product.active = data.get('active', product.active)
        product.updated_at = datetime.utcnow()
        return self.repo.save(product)

    def delete(self, id):
        product = self.repo.get_by_id(id)
        if not product:
            return False
        self.repo.delete(product)
        return True
