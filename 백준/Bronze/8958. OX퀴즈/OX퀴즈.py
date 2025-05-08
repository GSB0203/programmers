n=int(input())

for i in range(n):
    answer = 0
    c = 1
    s = list(input())
    for j in s:
        if j== 'O':
            answer += c
            c += 1
        else:
            c=1
            
    print(answer)