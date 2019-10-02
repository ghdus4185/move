# 문제 2

T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]

    max_total = 0

    # 기준 좌표
    for i in range(0, N - K + 1):
        for j in range(0, M - K + 1):

            total = 0

            for k in range(i, i + K):
                for m in range(j, j + K):
                    if i + 1 <= k < i + K - 1 and j + 1 <= m < j + K - 1:
                        continue
                    else:
                        total += board[k][m]

            if total > max_total:
                max_total = total

    print(f"#{tc} {max_total}")
