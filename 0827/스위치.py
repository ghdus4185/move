import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
switch = input().split()
student_num = int(input()) # 학생수
# 남학생은 1 여학생은 2
for i in range(student_num):
    s, n = map(int, input().split())
    if s == 1:
        for x in range(n-1, N, n):
            if switch[x] == '1':
                switch[x] = '0'
            else:
                switch[x] = '1'
    else:
        if switch[n-1] == '0':
            switch[n-1] = '1'
        else:
            switch[n-1] = '0'
        k = 1
        while 1:
            if n - 1 + k < N and n - 1 - k >= 0:
                if switch[n - 1 - k] == switch[n - 1 + k]:
                    if switch[n-1-k] == '1':
                        switch[n - 1 - k] = switch[n - 1 + k] = '0'
                    else:
                        switch[n - 1 - k] = switch[n - 1 + k] = '1'
                else:
                    break
                k += 1
            else:
                break

for j in range(len(switch)//20+1):
    print('{}'.format(" ".join(switch[20*j:20+20*j])))