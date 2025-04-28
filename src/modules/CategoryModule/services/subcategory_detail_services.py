import json
from datetime import datetime
from modules.CategoryModule.models.m_subcategory_detail import MSubCategoryDetail
from modules.CategoryModule.repositories.subcategory_detail_repository import SubcategoryDetailRepository
from modules.CategoryModule.repositories.product_repository import ProductRepository  
from modules.CategoryModule.repositories.subcategory_repository import SubcategoryRepository
from redis import Redis
from services.base_services import BaseService


class SubcategoryDetailService(BaseService):
    def __init__(self, db, redis_client: Redis = None):
        self.db = db
        self.repo = SubcategoryDetailRepository(db)
        self.product_repo = ProductRepository(db)
        self.subcategory_repo = SubcategoryRepository(db)
        self.redis = redis_client or Redis()
        self.db = db
        self.repo = SubcategoryDetailRepository(db)
        self.product_repo = ProductRepository(db)
        self.subcategory_repo = SubcategoryRepository(db)
        self.redis = redis_client
        super().__init__(MSubCategoryDetail, self.repo)

    def _check_quantity_threshold(self, sub_detail, user_name):
        product = self.product_repo.get_by_id(sub_detail.product_id)
        category_name =  self.subcategory_repo.get_by_id(sub_detail.subcategory_id).name
        used_quantity = sub_detail.quantity
        max_stock = self.repo.get_stock(sub_detail.product_id)

        if max_stock > 0 and used_quantity >= max_stock * 0.9:
            data = {
                "alert": "Cantidad supera el 90%",
                "category": category_name,
                "product": product.name,
                "used_by": user_name,
                "timestamp": datetime.utcnow().isoformat()
            }
            self.redis.publish("inventory_alerts", json.dumps(data))

    def create(self, data, user_name):
        sub_detail = MSubCategoryDetail(
            subcategory_id=data['subcategory_id'],
            product_id=data['product_id'],
            quantity=data['quantity'],
            unit_value=data['unit_value'],
            total_value=data['total_value'],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        saved = self.repo.create(sub_detail)
        # self._check_quantity_threshold(saved, user_name)
        return saved

    def update(self, id, data, user_name):
        sub_detail = self.repo.get_by_id(id)
        if not sub_detail:
            return None
        sub_detail.subcategory_id = data.get('subcategory_id', sub_detail.subcategory_id)
        sub_detail.product_id = data.get('product_id', sub_detail.product_id)
        sub_detail.quantity = data.get('quantity', sub_detail.quantity)
        sub_detail.unit_value = data.get('unit_value', sub_detail.unit_value)
        sub_detail.total_value = data.get('total_value', sub_detail.total_value)
        sub_detail.updated_at = datetime.utcnow()
        saved = self.repo.update(sub_detail)
        # self._check_quantity_threshold(saved, user_name)
        return saved
