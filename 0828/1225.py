import sys
sys.stdin = open('input.txt','r')

for _ in range(10):
    tc = int(input())
    data = list(map(int, input().split()))
    i = 1
    while 1:
        if i == 6:
            i = 1
        a = data.pop(0)
        if a - i > 0:
            data.append(a-i)
        else:
            data.append(0)
            break
        i += 1
    data = list(map(str, data))
    print('#{}'.format(tc), end=" ")
    for i in data:
        print('{}'.format(" ".join(i)), end=" ")
    print()