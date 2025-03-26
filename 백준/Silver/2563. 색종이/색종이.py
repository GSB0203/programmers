paper = [[0 for _ in range(100)] for _ in range(100)]
answer = 0

n = int(input())

for i in range(n):
    l, r = map(int, input().split())

    for j in range(l, l + 10):
        for k in range(r, r + 10):
            paper[j][k] = 1

for i in paper:
    answer += sum(i)

print(answer)