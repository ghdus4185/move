#항구에 들어오는 배
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    happy = [int(input()) for _ in range(N)]
    for i in happy[1:]:
        for j in range(2*i-1, happy[-1]+1, i-1):
            if j in happy:
                happy.remove(j)
    print('#{} {}'.format(tc+1, len(happy)-1))