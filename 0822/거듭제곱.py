def power(n):
    global M
    if n == 1:
        return 1
    else:
        return n ** M


for tc in range(10):
    t = int(input())
    N,M = map(int,input().split())
    print(f'#{tc+1} {power(N)}')