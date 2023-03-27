import pytest
from pydantic import ValidationError
from src.models.input import TextAnalysisInput

def test_invalid_service():
    with pytest.raises(ValidationError) as err:
        TextAnalysisInput(service="invalid-service", text="test")
