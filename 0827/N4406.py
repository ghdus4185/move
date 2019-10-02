import sys
sys.stdin = open('1_input_sample.txt','r')

T = int(input())
vowel = ['a','e','i','o','u']
for tc in range(T):
    result = ''
    a = input()
    for i in a:
        if i not in vowel:
            result += i
    print(f'#{tc+1} {result}')