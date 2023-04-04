def solution(numbers, target):
    answer = 0

    def dfs(idx, value):
        nonlocal answer
        if len(numbers) == idx and value == target:
            answer += 1
            return
        if len(numbers) == idx:
            return

        dfs(idx + 1, value + numbers[idx])
        dfs(idx + 1, value - numbers[idx])

    dfs(0, 0)

    return answer