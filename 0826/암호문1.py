import sys
sys.stdin = open('input.txt','r')

for tc in range(10):
    N = int(input())
    origin = input().split()
    order_num = int(input())
    order = input().split()

    idx = 0
    for i in range(order_num):
        if order[idx] == 'I':
            x = int(order[idx+1])
            y = int(order[idx+2])
            for j in range(y):
                origin.insert(x+j, order[idx+3+j])
            idx += 3 + y
    s = ' '.join(origin[:10])
    print(f'#{tc+1} {s}')
