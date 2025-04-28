from pydantic import BaseModel, Field, model_validator
from typing import Optional, Dict, Any
from datetime import datetime
from sqlalchemy.orm import Session
from modules.PermissionModule.models.m_actions import MAction
from modules.ParameterModule.models.m_parameters_values import MParameterValue

class MActionBaseValidator(BaseModel):
    code: str = Field(..., min_length=1, max_length=50)
    name: str = Field(..., min_length=1, max_length=100)
    type_id: Optional[int] = None
    active: bool

    @model_validator(mode='before')
    def strip_strings(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        # Opcional: quitar espacios en strings
        for field in ('code','name'):
            if field in values and isinstance(values[field], str):
                values[field] = values[field].strip()
        return values

    @model_validator(mode='after')
    def validate_alphanumeric(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        code = values.get("code")
        if code and not code.isalnum():
            raise ValueError("El código sólo puede contener letras y números")
        return values

class MActionCreateValidator(MActionBaseValidator):
    @model_validator(mode='after')
    def check_type_and_unique_code(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        db: Session = values.get("__db__")
        code = values["code"]
        type_id = values.get("type_id")
        if type_id is not None and not db.get(MParameterValue, type_id):
            raise ValueError(f"type_id {type_id} no existe en m_parameters_values")
        # Unicidad de code
        if db.query(MAction).filter(MAction.code == code).first():
            raise ValueError(f"El código '{code}' ya está registrado")
        return values

class MActionUpdateValidator(BaseModel):
    code: Optional[str] = Field(None, min_length=1, max_length=50)
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    type_id: Optional[int] = None
    active: Optional[bool] = None

    @model_validator(mode='after')
    def check_type_and_unique_code(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        db: Session = values.get("__db__")
        action_id: int = values.get("__id__")
        type_id = values.get("type_id")
        code = values.get("code")
        if type_id is not None and not db.get(MParameterValue, type_id):
            raise ValueError(f"type_id {type_id} no existe")
        if code is not None:
            exists = db.query(MAction).filter(
                MAction.code == code, MAction.id != action_id
            ).first()
            if exists:
                raise ValueError(f"El código '{code}' ya está registrado")
        return values

class MActionResponseValidator(MActionBaseValidator):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes  = True