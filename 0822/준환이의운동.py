import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for tc in range(T):
    L, U, X = map(int,input().split())
    if L<= X <= U:
        print(f'#{tc+1} 0')
    elif U <= X:
        print(f'#{tc+1} -1')
    else:
        print(f'#{tc+1} {L-X}')