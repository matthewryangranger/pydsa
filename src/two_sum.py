## Two Sum leetcode problem
### (https://leetcode.com/problems/two-sum/description/)

def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for index, number in enumerate(nums):
        complement: int = target - number
        if complement in seen:
            return [seen[complement], index]
        seen[number] = index
    return []