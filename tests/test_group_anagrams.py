from src.group_anagrams import group_anagrams


def test_group_anagrams_empty():
    # Given
    uncategorized_words: list[str] = [""]
    # When
    categorized_words: list[list[str]] = group_anagrams(uncategorized_words)
    # Then
    assert categorized_words == [[""]]

def test_group_anagrams_x():
    # Given
    uncategorized_words: list[str] = ["x"]
    # When
    categorized_words: list[list[str]] = group_anagrams(uncategorized_words)
    # Then
    assert categorized_words == [["x"]]


def test_group_anagrams_two_words():
    # Given
    uncategorized_words: list[str] = ["act","cat"]
    # When
    categorized_words: list[list[str]] = group_anagrams(uncategorized_words)
    # Then
    assert categorized_words == [["act", "cat"]]

def test_group_anagrams():
    # Given
    uncategorized_words: list[str] = ["act","pots","tops","cat","stop","hat"]
    # When
    categorized_words: list[list[str]] = group_anagrams(uncategorized_words)
    # Then
    assert categorized_words == sorted([["hat"],sorted(["act", "cat"]), sorted(["stop", "pots", "tops"])])