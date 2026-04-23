from src.contains_duplicate import contains_duplicate


def test_single_int_list():
    # Given
    single_int_list: list[int] = [1]
    # When
    result: bool = contains_duplicate(single_int_list)
    # Then
    assert result is False

def test_empty_list():
    # Given
    empty_list: list[int] = []
    # When
    result: bool = contains_duplicate(empty_list)
    # Then
    assert result is False

def test_duplicate_list():
    # Given
    duplicate_list: list[int] = [1, 2, 3, 4, 1]
    # When
    result: bool = contains_duplicate(duplicate_list)
    # Then
    assert result is True

def test_no_duplicate_list():
    # Given
    no_duplicate_list: list[int] = [1, 3, 2, 5]
    # When
    result: bool = contains_duplicate(no_duplicate_list)
    # Then
    assert result is False