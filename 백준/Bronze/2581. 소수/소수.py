def prime(p):
    if p < 2:
        return False
        
    for i in range(2, p):
        if p % i == 0:
            return False
            
    return True

m = int(input())
n = int(input())
p_sum = 0
p_min = 9999999

for i in range(m, n + 1):
    if prime(i):
        p_sum += i
        p_min = min(i, p_min)

if p_sum == 0:
    print(-1)
else:
    print(p_sum)
    print(p_min)
    