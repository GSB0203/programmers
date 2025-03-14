def divisor(number):
    count = 0
    for i in range(1, int(number ** (1 / 2)) + 1):
        if number % i == 0:
            count += 2 if i * i != number else 1
    return count

def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number + 1):
        if divisor(i) > limit:
            answer += power
        else:
            answer += divisor(i)
            
    return answer
