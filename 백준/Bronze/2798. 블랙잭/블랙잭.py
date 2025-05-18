n, m = map(int, input().split())
c = list(map(int, input().split()))
result = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for l in range(j + 1, n):
            s = c[i] + c[j] + c[l]
            if s > result and s <= m:
                result = s

print(result)