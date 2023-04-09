from collections import deque


def solution(tickets):
    answer = []
    flight = dict()

    for start, end in tickets:
        if start in flight:
            flight[start].append(end)
        else:
            flight[start] = [end]

    for r in flight.keys():
        flight[r].sort(reverse=True)

    stack = ["ICN"]
    path = []
    print(flight)
    while (stack):
        #스택에서 가장 위의 저장된 데이터를 거내오기
        top = stack.pop()
        #top이 그래프에 없거나, top을 시작점으로 하는 티켓이 없는 경우 path에 저장
        if top not in flight or len(flight[top]) == 0:
            path.append(top)
        #top을 다시 스택에 넣고 top의 도착점 중 가장 마지막 지점을 꺼내와 스택에 저장
        else:
            stack.append(top)
            stack.append(flight[top].pop())


    answer = path[::-1]

    return answer


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print("===============")
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
