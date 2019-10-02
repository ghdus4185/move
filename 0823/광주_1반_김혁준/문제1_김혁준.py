# 문제 1. 칠 영역의 개수 구하기

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    board = [list([0] * N) for _ in range(N)]

    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())

        # 인덱스로 하므로, x1 - 1 ~ x2 + 1 까지
        for i in range(x1 - 1, x2):
            # y1 - 1 ~ y2 + 1 까지
            for j in range(y1 - 1, y2):
                if board[i][j] != 1:
                    board[i][j] = 1
    total = 0
    for row in board:
        total += row.count(1)

    print(f"#{tc} {total}")
