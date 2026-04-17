from src.contains_duplicate import contains_duplicate


def test_single_int_list():
    # Given
    single_int_list: list[int] = [1]
    # When
    result: bool = contains_duplicate(single_int_list)
    # Then
    assert result is False