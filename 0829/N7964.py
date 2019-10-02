import sys
sys.stdin = open('input.txt', 'r')

# 부먹왕국의 차원문
T = int(input())
for tc in range(T):
    N, D = map(int, input().split())
    maps = list(map(int, input().split()))
    cnt = 0

    for i in range(N - D):
        if i == 0 and maps[i] == 0:
            maps[i] = 1
            cnt += 1

        if maps[i] == 1:
            if maps[i+D] != 1:
                maps[i+D] = 1
                cnt += 1

    print('#{} {}'.format(tc + 1, cnt))