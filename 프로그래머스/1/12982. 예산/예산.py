def solution(d, budget):
    d.sort()
    answer = 0
    
    for i in d:
        if budget - i < 0:
            return answer
        else:
            answer += 1
            budget -= i
            
    return answer