import sys
sys.stdin = open('input.txt','r')

for tc in range(10):
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int,input().split())))
    matrix_z = list(zip(*matrix))

    cnt = 0
    for i in range(N):
        for j in range(N-1):
            if matrix_z[i][j] == 1:
                for x in range(1,N-j):
                    if matrix_z[i][j+x] == 1:
                        break
                    elif matrix_z[i][j+x] == 2:
                        cnt +=1
                        break

    print(f'#{tc+1} {cnt}')