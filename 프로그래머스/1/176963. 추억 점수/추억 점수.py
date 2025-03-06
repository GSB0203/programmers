def solution(name, yearning, photo):
    answer = []
    score = {}
    
    for i in range(len(name)):
        score[name[i]] = yearning[i]
    
    for i in photo:
        totalScore = 0
        for j in i:
            totalScore += score.get(j, 0)
        answer.append(totalScore)
    
    return answer
