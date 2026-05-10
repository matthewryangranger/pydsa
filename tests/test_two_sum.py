import pytest

from src.two_sum import two_sum

@pytest.mark.skip(reason="Not implemented yet")
def test_two_nums_in_list():
    # Given
    nums: list[int] = [2, 7]
    target: int = 9
    # When
    result: list[int] = two_sum(nums, target)
    expected_result: list[int] = [0, 1]
    # Then
    assert result == expected_result