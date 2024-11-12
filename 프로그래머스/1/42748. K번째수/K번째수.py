def solution(array, commands):
    answer = []
    for command in commands:
        start, end, position = command
        subarray = sorted(array[start-1:end])
        answer.append(subarray[position-1])
    return answer
