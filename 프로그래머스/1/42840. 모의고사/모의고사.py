def solution(answers):
    member = [[1, 2, 3, 4, 5], 
              [2, 1, 2, 3, 2, 4, 2, 5], 
              [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    count = [0, 0, 0]
    answer = []
    
    for idx, ans in enumerate(answers):
        if ans == member[0][idx % len(member[0])]:
            count[0] += 1
        if ans == member[1][idx % len(member[1])]:
            count[1] += 1
        if ans == member[2][idx % len(member[2])]:
            count[2] += 1

    max_score = max(count)
    for i in range(3):
        if max_score == count[i]:
            answer.append(i + 1)
            
    return answer
