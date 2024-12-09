def solution(nums):
    answer = 0
    answer = list(set(nums))
    return len(answer) > len(nums) / 2 and len(nums) / 2 or len(answer)