def solution(s):
    answer = ""
    words = list(map(str, s.split(" ")))
    
    for i in words:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += " "
        
    return answer[:-1]