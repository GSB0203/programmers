def prime(p):
    if p < 2:
        return False
        
    for i in range(2, p):
        if p % i == 0:
            return False
            
    return True

    
n = int(input())
p = list(map(int, input().split()))
cnt = 0

for i in p:
    if prime(i):
        cnt += 1

print(cnt)