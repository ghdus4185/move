import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(T):
    N = int(input())
    room = list(map(int, input().split()))

    a = [0] * N
    idx = 1
    cnt = 0
    for i in room:
        if i != a[idx-1]:
            for j in range(idx, N+1, idx):
                if a[j-1] == 0:
                    a[j-1] = 1
                else:
                    a[j-1] = 0
            cnt += 1
        idx += 1

    print('#{} {}'.format(tc+1, cnt))