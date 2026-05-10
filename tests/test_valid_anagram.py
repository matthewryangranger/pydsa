from src.valid_anagram import valid_anagram

def test_valid_anagram_single_letter():
    assert valid_anagram("a", "a") is True

def test_invalid_anagram_double_letters():
    assert valid_anagram("ab", "bc") is False

def test_valid_anagram_double_letters():
    assert valid_anagram("ab", "ba") is True