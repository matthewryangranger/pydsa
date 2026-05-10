## House Robber leetcode problem
### (https://leetcode.com/problems/house-robber/description/)

def max(num1: int, num2: int) -> int:
    return num1 if num1 > num2 else num2

def rob(nums: list[int]) -> int:
    max_amount_even: int = 0
    max_amount_odd: int = 0
    index: int = 0
    for num in nums:
        if index % 2 == 0:
            max_amount_even += num
        else:
            max_amount_odd += num
        index += 1

    return max(max_amount_even, max_amount_odd)