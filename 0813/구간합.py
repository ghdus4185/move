import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    n,m = map(int, input().split())
    numbers = list(map(int, input().split()))
    lists=[]
    for i in range(n-m+1):
        max_num = 0
        for j in range(m):
            max_num = max_num + numbers[i+j]
        lists.append(max_num)
        result = max(lists) - min(lists)
    print('#{} {}'.format(test_case, result))