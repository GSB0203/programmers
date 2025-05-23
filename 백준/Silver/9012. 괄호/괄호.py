t = int(input())

for i in range(t):
    s = []
    a = input()
    for j in a:
        if j == '(':
            s.append(j)
        elif j == ')':
            if s:
                s.pop()
            else:
                print("NO")
                break
    else:
        if not s:
            print("YES")
        else:
            print("NO")