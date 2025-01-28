def solution(a, b, n):
    answer = 0
    
    while(n):
        n -= a
        n += b
        answer += b
        if n < a:
            return answer
