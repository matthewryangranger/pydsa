## House Robber leetcode problem
### (https://leetcode.com/problems/house-robber/description/)

def rob(nums: list[int]) -> int:
    max_amount: int = 0
    index: int = 0
    for num in nums:
        if index == 0:
            max_amount = num
        if num > max_amount:
            max_amount = num
    return max_amount