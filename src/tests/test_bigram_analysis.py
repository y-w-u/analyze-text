from src.services.bigram_analysis import bigram_analysis


def test_bigram_analysis_simple():
    text = "The quick brown fox jumps over the lazy dog."
    expected_result = [
        ["the", "quick"],
        ["quick", "brown"],
        ["brown", "fox"],
        ["fox", "jumps"],
        ["jumps", "over"],
        ["over", "the"],
        ["the", "lazy"],
        ["lazy", "dog"],
    ]
    assert bigram_analysis(text) == expected_result

def test_bigram_analysis_with_different_freqs():
    text = "@The quick brown fox jumps over the lazy dog../* The quick brown fox jumps over the lazy dog again and again. The quick brown"
    expected_result = [
        ["the", "quick"],
        ["quick", "brown"]
    ]
    assert bigram_analysis(text) == expected_result

def test_bigram_analysis_with_one_word():
    text = "!The .\ "
    expected_result = []
    assert bigram_analysis(text) == expected_result

def test_bigram_analysis_with_empty_string():
    text = ""
    expected_result = []
    assert bigram_analysis(text) == expected_result

def test_bigram_analysis_with_only_symbols():
    text = ".*&^"
    expected_result = []
    assert bigram_analysis(text) == expected_result
