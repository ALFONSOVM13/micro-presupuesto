# from pydantic import BaseModel, Field, validator
# from typing import Optional
# from datetime import datetime


# class RegionBase(BaseModel):
#     code: str = Field(..., max_length=255, description="Código de la región")
#     name: str = Field(..., max_length=255, description="Nombre de la región")
#     active: Optional[bool] = Field(default=True, description="Estado activo")

#     @validator("code", "name")
#     def not_empty(cls, v, field):
#         if not v.strip():
#             raise ValueError(f"El campo '{field.name}' no puede estar vacío.")
#         return v


# class RegionCreate(RegionBase):
#     pass


# class RegionUpdate(BaseModel):
#     code: Optional[str] = Field(None, max_length=255)
#     name: Optional[str] = Field(None, max_length=255)
#     active: Optional[bool]

#     @validator("code", "name")
#     def validate_optional_not_empty(cls, v, field):
#         if v is not None and not v.strip():
#             raise ValueError(f"El campo '{field.name}' no puede estar vacío si se proporciona.")
#         return v


# class RegionResponse(RegionBase):
#     id: int
#     created_at: datetime
#     updated_at: datetime

#     class Config:
#         orm_mode = True
