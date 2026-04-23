from src.house_robber import rob


def test_empty_house_list():
    # Given
    empty_list: list[int] = []
    # When
    result: int = rob(empty_list)
    # Then
    assert result is 0