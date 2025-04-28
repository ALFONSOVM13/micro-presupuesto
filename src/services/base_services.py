# services/base_service.py

from typing import Type, TypeVar, List, Optional, Dict, Any
from repositories.base_repository import BaseRepository

Model = TypeVar("Model")
CreateSchema = TypeVar("CreateSchema")
UpdateSchema = TypeVar("UpdateSchema")

class BaseService:

    def __init__(self, model: type[Model], repository_cls: Type[BaseRepository]):
        self.model = model
        self.repo: BaseRepository = repository_cls

    def get_all(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order_by: Optional[str] = None,
        filters: Optional[Dict[str, Any]] = None
    ) -> List[Model]:
        return self.repo.get_all(
            limit=limit,
            offset=offset,
            order_by=order_by,
            filters=filters
        )

    def get_by_id(self, entity_id: int) -> Optional[Model]:
        return self.repo.get_by_id(entity_id)
