from fastapi import APIRouter, HTTPException
from src.models.input import TextAnalysisInput
from src.models.service_type import ServiceType
from src.services import bigram_analysis, word_count_analysis

router = APIRouter()


@router.post("")
async def analyze_text(data: TextAnalysisInput):
    if not data.text:
        raise HTTPException(status_code=400, detail="text field cannot be empty.")

    result = None
    if data.service == ServiceType.bigram:
        result = bigram_analysis(data.text)
    elif data.service == ServiceType.word_count:
        result = word_count_analysis(data.text)
    return {"result": result}
