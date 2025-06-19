def solution(log):
    answer = ''
    numLog = dict(zip([1, -1, 10, -10], ['w', 's', 'd', 'a']))

    for i in range(1, len(log)):
        answer += numLog[log[i] - log[i-1]]
        
    return answer