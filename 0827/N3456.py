import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for tc in range(T):
    matrix = list(map(int, input().split()))
    for i in matrix:
        if matrix.count(i) == 1 or matrix.count(i) == 3:
            length = i
    print(f'#{tc+1} {length}')