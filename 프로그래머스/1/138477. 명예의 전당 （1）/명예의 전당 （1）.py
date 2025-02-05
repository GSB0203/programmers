def solution(k, score):
    result = []
    answer = []
    
    for i in score:
        result.append(i)
        result.sort(reverse=True)
        if len(result) < k:
            answer.append(result[-1])
        else:
            answer.append(result[k-1])
    
    return answer
