def solution(n):
    answer = n
    while(1):
        answer += 1
        if bin(n).count("1") == bin(answer).count("1"):
            return answer