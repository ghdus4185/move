import sys
sys.stdin = open('input1.txt','r')

T = int(input())
for tc in range(T):
    N,K = map(int, input().split())
    fly = [list(map(int,input().split())) for i in range(N)]
    maxV = 0
    for i in range(0,N-K+1): #부분 영역의 왼쪽 위 모서리칸 좌표, i, j
        for j in range(0,N-K+1):
            s = 0
            for x in range(K):
                if x == 0:
                    s += sum(fly[i+x][j:j+K])
                else:
                    s += fly[i+x][j+K-1]
            if maxV < s:
                maxV = s
    print(f'#{tc+1} {maxV}')