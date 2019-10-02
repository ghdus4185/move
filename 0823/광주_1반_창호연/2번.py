import sys
sys.stdin = open('input2.txt','r')

T = int(input())
for tc in range(T):
    matrix = []
    N, M, K = map(int, input().split())
    for i in range(N):
        matrix.append(list(map(int, input().split())))

    maxV = 0
    for i in range(N-K+1):
        for j in range(N-K+1):
            s = 0
            for x in range(K):
                if x==0 or x ==K-1:
                    s += sum(matrix[i+x][j:j+K])
                else:
                    s += matrix[i+x][j] + matrix[i+x][j+K-1]
            if maxV < s:
                maxV = s
    print('#{} {}'.format(tc+1,maxV))
