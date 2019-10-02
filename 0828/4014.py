T = int(input())
for tc in range(T):
    N, X = map(int, input().split()) # 6<= N <= 20, 2<= X <=4
    matrix = [list(map(int, input().split())) for _ in range(N)]
    matrix_z = list(zip(*matrix))
    for i in range(N):
        cnt = 0
        for j in range(N-1):
            if matrix[i][j] == matrix [i][j+1]:
                res = 1
            if res == 1:
                cnt += 1
                res = 0

            if matrix[i][j] != matrix[i][j+1] and abs(matrix[i][j]-matrix[i][j+1]) == 1:





    # print('#{} {}'.format(tc+1, res))