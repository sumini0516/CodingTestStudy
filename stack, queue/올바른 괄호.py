def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == "(":
            stack.append(1)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) > 0:
        return False

    return True