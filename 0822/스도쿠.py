import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(T):
    matrix = []
    for i in range(9):
        matrix.append(list(map(int,input().split())))
    matrix_z = list(zip(*matrix))

    check = 1

    # 네모 검사
    while check == 1:
        for i in range(3):
            for j in range(3):
                s = 0
                for x in range(3):
                    s += sum(matrix[i*3+x][j*3:j*3+3])
                if s != 45:
                    check = 0
                    break
        # 가로, 세로 검사
        for i in range(9):
            s1 = 0
            s2 = 0
            s1 += sum(matrix[i][::])
            s2 += sum(matrix_z[i][::])
            if s1 != 45 or s2 != 45:
                check = 0
                break

    print(f'#{tc+1} {check}')