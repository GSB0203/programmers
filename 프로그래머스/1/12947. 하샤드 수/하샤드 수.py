def solution(x):
    return x % sum(list(map(int, str(x)))) == 0 or True and False