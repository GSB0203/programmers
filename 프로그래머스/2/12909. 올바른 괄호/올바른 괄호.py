def solution(s):
    stack = []
    
    for i in s:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if not stack:
                return False
            elif stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')

    return len(stack) == 0
