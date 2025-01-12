def solution(s):
    numbers = list(map(int, s.split()))
    
    min_numbers = min(numbers)
    max_numbers = max(numbers)
    
    return str(min_numbers) + ' ' + str(max_numbers)

