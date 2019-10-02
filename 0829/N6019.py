T = int(input())
for tc in range(T):
    D, A, B, F = map(int, input().split())
    X = D / (A + B)
    result = F * X
    print('#{} {}'.format(tc+1, result))
