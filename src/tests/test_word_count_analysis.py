from src.services.word_count_analysis import word_count_analysis


def test_word_count_analysis():
    text = "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog again and again."
    expected_result = {
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
    assert word_count_analysis(text) == expected_result

def test_word_count_analysis_with_empty_string():
    text = ""
    expected_result = {}
    assert word_count_analysis(text) == expected_result

def test_word_count_analysis_with_only_symbols():
    text = ".*&^"
    expected_result = {}
    assert word_count_analysis(text) == expected_result
