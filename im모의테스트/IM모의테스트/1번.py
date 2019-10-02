import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    matrix = [[0] * M for _ in range(N)]
    maxV = 0
    for x in range(K):
        color = list(map(int, input().split()))

        res = 0
        for i in range(color[2]-color[0]+1):
            for j in range(color[3]-color[1]+1):
                if matrix[color[0]+i][color[1]+j] > color[4]:
                    res = 1
        if res == 0:
            for i in range(color[2]-color[0]+1):
                for j in range(color[3]-color[1]+1):
                    if matrix[color[0]+i][color[1]+j] <= color[4]:
                        matrix[color[0]+i][color[1]+j] = color[4]

    for z in range(11):
        add = 0
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == z:
                    add += 1
        if maxV <= add:
            maxV = add

    print('#{} {}'.format(tc+1, maxV))