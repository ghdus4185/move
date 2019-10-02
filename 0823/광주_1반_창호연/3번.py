import sys
sys.stdin = open('input3.txt','r')

T = int(input())
for tc in range(T):
    N = int(input())
    matrix = []
    cntS = 0
    # N * N matrix 생성
    for i in range(N):
        matrix.append(list(map(int,input().split())))

    # 섬을 만들고 cntS += 1
    #그 주변 8 방향을 탐색
    for i in range(N):
        for j in range(N):
            #matrix를 돌다가 0이 아닌값을 찾음
            if matrix[i][j] != 0:
                while 1:
                    #그 값을 0으로 만들어주고
                    matrix[i][j] = 0
                    # 만약 위에가 0이 아니면 위로 이동
                    if 0< i and matrix[i-1][j] != 0:
                        i = i-1
                    # 오른쪽 이동
                    elif j < N-1 and matrix[i][j+1] != 0:
                        j = j+1
                    # 왼쪽 이동
                    elif j > 0 and matrix[i][j-1] != 0:
                        j = j-1
                    # 밑 이동
                    elif i < N-1 and matrix[i+1][j] != 0:
                        i = i+1
                    # 오른 대각 밑 이동
                    elif i < N-1 and j < N-1 and matrix[i+1][j+1] != 0:
                        i = i+1
                        j = j+1
                    #왼쪽 대각 밑 이동
                    elif i < N-1 and j > 0 and matrix[i+1][j-1] != 0:
                        i = i+1
                        j = j-1
                    # 오른쪽 대각 위 이동
                    elif 0 < i and j < N-1 and matrix[i-1][j+1] != 0:
                        i = i-1
                        j = j+1
                    # 왼쪽 대각 위 이동
                    elif i > 0 and j > 0 and matrix[i-1][j-1] != 0:
                        i = i-1
                        j = j-1
                    else:
                        cntS += 1
                        break
    print('#{} {}'.format(tc+1, cntS))