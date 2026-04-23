from src.house_robber import rob


def test_empty_house_list():
    # Given
    empty_list: list[int] = []
    # When
    result: int = rob(empty_list)
    # Then
    assert result is 0

def test_two_house_list():
    # Given
    house_list: list[int] = [0, 1]
    # When
    result: int = rob(house_list)
    # Then
    assert result is 1

def test_three_house_list():
    # Given
    house_list: list[int] = [0, 5, 2]
    # When
    result: int = rob(house_list)
    # Then
    assert result is 5