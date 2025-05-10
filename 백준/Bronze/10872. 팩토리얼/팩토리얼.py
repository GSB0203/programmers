def f(n):
    x = 1
    if n > 0 :
        x = n * f(n - 1)
    return x

n = int(input())
print(f(n))