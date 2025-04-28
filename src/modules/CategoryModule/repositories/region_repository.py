from modules.CategoryModule.models.m_regions import MRegion
from repositories.base_repository import BaseRepository
class RegionRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(db, MRegion)

    def get_by_id(self, region_id: int):
        return self.db.query(MRegion).filter(MRegion.id == region_id).first()

    def create(self, region: MRegion):
        self.db.add(region)
        self.db.commit()
        self.db.refresh(region)
        return region

    def update(self, region_id: int, data: dict):
        region = self.get_by_id(region_id)
        if not region:
            return None
        for key, value in data.items():
            setattr(region, key, value)
        self.db.commit()
        self.db.refresh(region)
        return region

    def delete(self, region_id: int):
        region = self.get_by_id(region_id)
        if not region:
            return None
        self.db.delete(region)
        self.db.commit()
        return region
