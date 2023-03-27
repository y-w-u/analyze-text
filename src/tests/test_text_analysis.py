import asynctest
import json
import pytest
from fastapi import HTTPException
from src.models.input import TextAnalysisInput
from src.routers.text_analysis import analyze_text


def convert_to_json(value):
    return json.dumps(value, sort_keys=True)

@pytest.mark.asyncio
@asynctest.patch("src.routers.text_analysis.bigram_analysis")
async def test_bigram_analysis(mock_bigram_analysis):
    data = TextAnalysisInput(service="bigram", text="The quick brown fox jumps over the lazy dog.")
    expected_result = [["the", "quick"]]
    mock_bigram_analysis.return_value = expected_result

    assert convert_to_json(await analyze_text(data)) == convert_to_json({"result": expected_result})


@pytest.mark.asyncio
@asynctest.patch("src.routers.text_analysis.word_count_analysis")
async def test_word_count_analysis(mock_word_count_analysis):
    data = TextAnalysisInput(service="word-count", text="The quick brown fox jumps over the lazy dog.")
    expected_result = {"the": 2, "quick": 1, "brown": 1}
    mock_word_count_analysis.return_value = expected_result

    assert convert_to_json(await analyze_text(data),) == convert_to_json({"result": expected_result})


@pytest.mark.asyncio
async def test_empty_text():
    data = TextAnalysisInput(service="bigram", text="")
    with pytest.raises(HTTPException) as err:
        await analyze_text(data)
        assert err.value.status_code == 400
        assert err.value.detail == "text field cannot be empty."
