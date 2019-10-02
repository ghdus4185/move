import sys
sys.stdin = open('sample_input.txt', 'r')

#현주의 상자 바꾸기
T = int(input())
for tc in range(T):
    N, Q = map(int, input().split())
    box = [0] * N
    for _ in range(Q):
        L, R = map(int, input().split())
        i = _ + 1

# L번 박스부터 R번 박스까지를 0 -> i로 변경
        for x in range(L-1, R):
            box[x] = i

    box = list(map(str, box))
    res = " ".join(box)
    print('#{} {}'.format(tc+1, res))