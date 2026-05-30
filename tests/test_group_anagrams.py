import pytest

from src.group_anagrams import group_anagrams

@pytest.mark.skip(reason="Not implemented yet")
def test_group_anagrams():
    # Given
    uncategorized_words: list[str] = ["act","pots","tops","cat","stop","hat"]
    # When
    categorized_words: list[list[str]] = group_anagrams(uncategorized_words)
    # Then
    assert categorized_words == [["hat"],["act", "cat"],["stop", "pots", "tops"]]