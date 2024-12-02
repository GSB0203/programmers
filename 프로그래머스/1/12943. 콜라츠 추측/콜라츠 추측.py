def solution(num):
    answer = 0
    collatz = []
    
    if answer == 1:
        return 0
    
    while(num != 1):
        collatz.append(num)
        answer += 1
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1
            
    if answer >= 500:
            return -1

    return answer