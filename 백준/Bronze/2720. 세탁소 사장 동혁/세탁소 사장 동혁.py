n = int(input())
change = [25, 10, 5, 1]

for i in range(n):
    c = int(input())
    for j in change:
        print(int(c // j), end=" ")
        c %= int(j)
    print()