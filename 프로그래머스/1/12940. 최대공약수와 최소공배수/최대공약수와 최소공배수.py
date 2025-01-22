def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

def solution(n, m):
    answer = []
    answer.append(gcd(n, m))
    answer.append(n * m // gcd(n, m))
    return answer