def solution(nums):
    answer = set(nums)
    return len(answer) > len(nums) / 2 and len(nums) / 2 or len(answer)