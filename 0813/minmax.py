import sys
sys.stdin = open('sample_input.txt','r')

t = int(input())
for a in range(1,t+1):
    count_num = int(input())
    num_li = list(map(int, input().split()))
    for i in range(count_num - 1):
        for j in range(count_num-1-i):
            temp = 0
            if num_li[j] > num_li[j+1]:
                temp = num_li[j]
                num_li[j] = num_li[j+1]
                num_li[j+1] = temp
        result = num_li[-1] - num_li[0]
    print('#{} {}'.format(a,result))