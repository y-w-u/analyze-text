from pydantic import BaseModel
from src.models.service_type import ServiceType


class TextAnalysisInput(BaseModel):
    service: ServiceType
    text: str
