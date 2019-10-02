T = int(input())
for tc in range(T):
    A, B = list(map(int, input().split()))
    print('#{} {}'.format(tc+1, A+B))