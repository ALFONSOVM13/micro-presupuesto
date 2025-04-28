from modules.CategoryModule.models.m_products import MProduct
from repositories.base_repository import BaseRepository

class ProductRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(db, MProduct)


    def get_by_id(self, id):
        return self.db.query(MProduct).filter(MProduct.id == id).first()

    def get_stock(self, id):
        product = self.get_by_id(id)
        if product:
            return product.stock
        return 0
    
    def save(self, product):
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def delete(self, product):
        self.db.delete(product)
        self.db.commit()
