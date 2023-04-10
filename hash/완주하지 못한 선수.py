def solution(participant, completion):
    answer = ''
    dict = {}
    participant.sort()
    completion.sort()

    for c in completion:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1

    for p in participant:
        if p in dict:
            if dict[p] >= 1:
                dict[p] -= 1
            else:
                answer = p
                break
        else:
            answer = p
            break

    return answer