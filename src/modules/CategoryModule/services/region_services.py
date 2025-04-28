from modules.CategoryModule.models.m_regions import MRegion
from modules.CategoryModule.repositories.region_repository import RegionRepository
from datetime import datetime
from services.base_services import BaseService
class RegionService(BaseService):
    def __init__(self, db):
        self.repository = RegionRepository(db)
        super().__init__(MRegion, self.repository)
        
        
    def list_regions(self, limit, offset, order_by, filters=None):
        return self.repository.get_all(limit=limit, offset=offset, order_by=order_by, filters=filters)

    def get_region(self, region_id):
        return self.repository.get_by_id(region_id)

    def create_region(self, data):
        new_region = MRegion(
            code=data["code"],
            name=data["name"],
            active=data.get("active", True),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        return self.repository.create(new_region)

    def update_region(self, region_id, data):
        data["updated_at"] = datetime.now()
        return self.repository.update(region_id, data)

    def delete_region(self, region_id):
        return self.repository.delete(region_id)
