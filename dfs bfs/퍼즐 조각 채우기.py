import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(i, j, graph, position, n, num):
    res = [position]

    for k in range(4):
        nx, ny = i + dx[k], j + dy[k]

        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == num:
            graph[nx][ny] = 2
            res = res + dfs(nx, ny, graph, [position[0] + dx[k], position[1] + dy[k]], n, num)

    return res


def rotate(lst):
    n = len(lst)

    #회전한 테이블
    o = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            o[j][n - 1 - i] = lst[i][j]

    return o


def solution(game_board, table):
    answer = 0
    n = len(game_board)
    game_board_copy = copy.deepcopy(game_board)
    block = []


    # 블록에 있는 빈 칸 저장
    for i in range(n):
        for j in range(n):
            if game_board_copy[i][j] == 0:
                game_board_copy[i][j] = 2
                result = dfs(i, j, game_board_copy, [0, 0], n, 0)[1:]
                print(result)
                block.append(result)

    for r in range(4):
        table = rotate(table)
        table_rotate_copy = copy.deepcopy(table)

        for i in range(n):
            for j in range(n):
                if table_rotate_copy[i][j] == 1:
                    table_rotate_copy[i][j] = 2
                    result = dfs(i, j, table_rotate_copy, [0, 0], n, 1)[1:]
                    if result in block:
                        block.pop(block.index(result))
                        answer += (len(result) + 1)
                        table = copy.deepcopy(table_rotate_copy)
                    else:
                        table_rotate_copy = copy.deepcopy(table)

    return answer


# ans = solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0],
#           [0, 1, 1, 1, 0, 0]],
#          [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0],
#           [0, 1, 0, 0, 0, 0]])
#
# print(ans)
