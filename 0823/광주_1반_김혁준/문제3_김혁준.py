# 문제 3

def BFS(board, N):
    visited = [[0] * N for _ in range(N)]
    land_count = 0

    for i in range(N):
        for j in range(N):

            # 숫자가 0 이상 + 아직 방문 안한곳이라면
            if board[i][j] > 0 and visited[i][j] == 0:
                land_count += 1  # 이곳은 섬이다.
                q = [[i, j]]

                # 이어진 모든곳을 살핀다.
                while q:
                    x, y = q.pop(0)

                    if board[x][y] > 0 and visited[x][y] == 0:
                        visited[x][y] = land_count

                    d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

                    for direction in d:
                        dx, dy = direction
                        ni = x + dx
                        nj = y + dy

                        if 0 <= ni < N and 0 <= nj < N:
                            if board[ni][nj] > 0 and visited[ni][nj] == 0 and [ni, nj] not in q:
                                q.append([ni, nj])

    return land_count


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]

    print(f"#{tc} {BFS(board, N)}")
