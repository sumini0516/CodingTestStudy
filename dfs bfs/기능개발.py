import math

def solution(progresses, speeds):
    answer = [0] * (len(speeds) + 1)
    todo = []
    max_progress = 0
    day = 0
    aa =[]

    for i in range(len(progresses)):
        td = math.ceil((100 - progresses[i]) / speeds[i])
        todo.append(td)
    print(todo)
    for i in todo:
        if i > max_progress:
            day += 1
            answer[day] += 1
            max_progress = i
        else:
            answer[day] += 1

    for i in answer:
        if i > 0 :
            aa.append(i)

    return aa

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))
