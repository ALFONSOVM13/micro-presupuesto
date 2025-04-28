from modules.FlowModule.models.m_flow_object_states import MFlowObjectState
from repositories.base_repository import BaseRepository


class FOSRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(db, MFlowObjectState)

