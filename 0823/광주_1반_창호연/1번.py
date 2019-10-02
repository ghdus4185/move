import sys
sys.stdin = open('input1.txt','r')

T = int(input())
for tc in range(T):
    N,M = map(int, input().split())

    matrix = []
    for i in range(N):
        matrix.append([0 for i in range(N)])
    s = 0
    for i in range(M):
        a = list(map(int,input().split()))

        for i in range(a[2]-a[0]+1):
            for j in range(a[3]-a[1]+1):
                matrix[a[0]+i][(a[1]+j)] = 1
    for i in range(N):
        s += sum(matrix[i][::])

    print('#{} {}'.format(tc + 1, s))