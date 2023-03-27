import json
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_bigram_analysis():
    response = client.post(
        "/analyze-text",
        data=json.dumps(
            {
                "service": "bigram",
                "text": "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog again and again. the quick brown",
            }
        ),
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "result": [
            ["the", "quick"],
            ["quick", "brown"]
        ]
    }


def test_word_count_analysis():
    response = client.post(
        "/analyze-text",
        data=json.dumps(
            {
                "service": "word-count",
                "text": "The ^&quick brown fox jumps over the lazy dog.,. the Quick brown fox jumps over the lazy dog again and again.",
            }
        ),
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "result": {
            "the": 4,
            "quick": 2,
            "brown": 2,
            "fox": 2,
            "jumps": 2,
            "over": 2,
            "lazy": 2,
            "dog": 2,
            "again": 2,
            "and": 1,
        }
    }


def test_invalid_service():
    response = client.post(
        "/analyze-text", json={"service": "invalid-service", "text": "The quick brown fox jumps over the lazy dog."}
    )

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "service"],
                "msg": "value is not a valid enumeration member; permitted: 'bigram', 'word-count'",
                "type": "type_error.enum",
                "ctx": {"enum_values": ["bigram", "word-count"]},
            }
        ]
    }


def test_missing_service():
    response = client.post("/analyze-text", json={"text": "The quick brown fox jumps over the lazy dog."})

    assert response.status_code == 422


def test_missing_text():
    response = client.post("/analyze-text", json={"service": "bigram"})

    assert response.status_code == 422

def test_empty_text():
    response = client.post("/analyze-text", json={"service": "bigram", "text": ""})

    assert response.status_code == 400
    assert response.text == '{"detail":"text field cannot be empty."}'
