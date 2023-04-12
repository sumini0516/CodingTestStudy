import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(i, j, graph, position, n, num):
    res = [position]

    for k in range(4):
        nx = dx[k] + i
        ny = dy[k] + j

        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == num:
            graph[nx][ny] = 2
            res = res + dfs(nx, ny, graph, [position[0] + dx[k], position[1] + dy[k]], n, num)

    return res


def rotate(lst):
    n = len(lst)

    new_table = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new_table[j][n - 1 - i] = lst[i][j]

    return new_table


def solution(game_board, table):
    answer = 0
    n = len(game_board)
    game_board_copy = copy.deepcopy(game_board)
    block = []

    # game_board에 있는 빈 칸의 모양 저장
    for i in range(n):
        for j in range(n):
            # game_board가 빈칸이면 dfs로 빈 곳 마저 탐색
            if game_board_copy[i][j] == 0:
                game_board_copy[i][j] = 2
                result = dfs(i, j, game_board_copy, [0, 0], n, 0)[1:]
                block.append(result)

    print(block)

    for r in range(4):
        table = rotate(table)
        table_copy = copy.deepcopy(table)

        for i in range(n):
            for j in range(n):
                if table_copy[i][j] == 1:
                    table_copy[i][j] = 2
                    result = dfs(i, j, table_copy, [0, 0], n, 1)[1:]
                    if result in block:
                        answer += len(result) + 1
                        block.pop(block.index(result))
                        table = copy.deepcopy(table_copy)
                    else:
                        table_copy = copy.deepcopy(table)

    return answer


ans = solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0, 0]],
               [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0],
                [0, 1, 0, 0, 0, 0]])

print(ans)
