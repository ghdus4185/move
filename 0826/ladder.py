import sys
sys.stdin = open('input.txt','r')

for tc in range(10):
    tc_num = int(input())
    matrix = []
    for i in range(100):
        matrix.append(input())

    di = [0, 0, -1]
    dj = [1, -1, 0]
    # start point
    for x in range(100):
        if matrix[99][x] == '2':
            start = x
            break
    
    k = 2
    layer = 99
    while x != 0:
        x -= 1
        if k == 2:
            layer -= 1
            for m in range(2):
                nj = y + dj[m]
                if nj >= 0 and nj < 100 and matrix[x][nj] =='1':
                    k = m
                    break
        else:
            if k == 0:
                nj = nj + dj[0]
            if k == 1:
                nj = nj + dj[1]
            y = nj
        if matrix[x - 1][nj] == '1':
            k = 2

    print(f'#{tc+1} {nj}')