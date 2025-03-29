n, k = map(int, input().split())
factor = []
for i in range(1, n + 1):
    if n % i == 0:
        factor.append(i)

print(factor[k - 1]) if len(factor) >= k else print(0)