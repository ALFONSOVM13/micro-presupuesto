from sqlalchemy.orm import Session

class BaseRepository:
    def __init__(self, db: Session, model):
        self.db = db
        self.model = model

    def get_all(self, limit: int = None, offset: int = None, order_by: str = None, filters: dict = None):
        query = self.db.query(self.model)

        if filters:
            for key, value in filters.items():
                column = getattr(self.model, key, None)
                if column is not None and value is not None:
                    query = query.filter(column == value)

        if order_by:
            order_column, order_direction = order_by.split(":")
            column = getattr(self.model, order_column, None)
            if column is not None:
                if order_direction.lower() == "desc":
                    query = query.order_by(column.desc())
                else:
                    query = query.order_by(column.asc())

        total = query.count()

        if limit is not None:
            query = query.limit(limit)
        if offset is not None:
            query = query.offset(offset)

        return query.all(), total

    def get_by_id(self, id: int):
        return self.db.query(self.model).filter(self.model.id == id).first()

    def create(self, data: dict):
        instance = self.model(**data)
        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)
        return instance

    def update(self, id: int, data: dict):
        instance = self.get_by_id(id)
        if not instance:
            return None

        for key, value in data.items():
            setattr(instance, key, value)

        self.db.commit()
        self.db.refresh(instance)
        return instance

    def delete(self, id: int):
        instance = self.get_by_id(id)
        if not instance:
            return None

        self.db.delete(instance)
        self.db.commit()
        return True
