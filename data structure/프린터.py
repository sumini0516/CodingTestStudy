def solution(priorities, location):

    seq = [i for i in range(len(priorities))]
    ans = []

    while priorities:
        current = priorities.pop(0)
        s = seq.pop(0)
        if not priorities:
            ans.append(s)
            break
        if current < max(priorities):
            priorities.append(current)
            seq.append(s)
        else:
            ans.append(s)
    answer = ans.index(location) + 1

    return answer
