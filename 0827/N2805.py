import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(T):
    N = int(input())
    matrix = [list(map(int,list(input()))) for _ in range(N)]

    value = 0
    for i in range(N):
        if i <= N//2:
            value += sum(matrix[i][N // 2 - i:N // 2 + i + 1])
        elif i > N//2:
            value += sum(matrix[i][0+(i - N//2):N-(i - N//2)])
    print('#{} {}'.format(tc+1,value))