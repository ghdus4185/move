import sys
sys.stdin = open('input.txt','r')

for tc in range(10):
    test_case = int(input())
    matrix = [input().split() for _ in range(100)]

    di = [0,0.-1]
    dj = [1,-1,0]
    k = 2

    #시작점
    for j in range(100):
        if matrix[99][j] == '2':
            start = j
            break

    layer = 99
    while layer != 0:
        if k == 2:
            layer -= 1
            for i in range(2):
                nj = start + dj[i]
                if nj >= 0 and nj < 100:
                    if matrix[layer][nj] == '1':
                        k = i
                        break
        else:
            if k == 0:
                nj = nj + dj[0]

            elif k == 1:
                nj = nj + dj[1]
            start = nj
        if matrix[layer - 1][nj] == '1':
            k = 2
    print('#{} {}'.format(test_case, nj+1))
