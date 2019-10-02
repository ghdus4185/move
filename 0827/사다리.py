import sys
sys.stdin = open('input.txt', 'r')

di = [-1, 0, 0]
dj = [0, 1, -1]
for tc in range(10):
    tc = input()
    N = 100
    ladder = [input().split() for _ in range(N)]
    k = 0
    #시작점 찾기
    for i in range(N):
        if ladder[N-1][i] == '2':
            start = i
            break

    layer = N-1

    #x가 0이 되면 도착

    while layer != 0:
        if k == 0:
            layer -= 1
            for i in range(1,3):
                nj = start + dj[i]
                if nj >= 0 and nj < N:
                    if ladder[layer][nj] == '1':
                        k = i
                        break
        else:
            if k == 1:
                nj = nj + dj[1]
            if k == 2:
                nj = nj + dj[2]
            start = nj
        if ladder[layer - 1][nj] == '1':
            k = 0
    print('#{} {}'.format(tc,nj+1))