n, b = map(int, input().split())
answer = ''
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while n:
    answer += str(arr[n % b])
    n //= b

print(answer[::-1])