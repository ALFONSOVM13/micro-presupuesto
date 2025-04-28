from modules.ParameterModule.models.m_parameters_values import MParameterValue
from repositories.base_repository import BaseRepository

class ParameterValueRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(db, MParameterValue)

