import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for tc in range(T):
    n = input()
    card = {'S':0, 'D':0, 'H':0, 'C':0}
    idx = 0
    result = 0
    for i in range(len(n)//3):
        if n.count(n[idx*3:idx*3+3]) == 1:
            a = n[idx * 3:idx * 3 + 3]
            if 'S' in a:
                card['S'] += 1
            elif 'D' in a:
                card['D'] += 1
            elif 'H' in a:
                card['H'] += 1
            elif 'C' in a:
                card['C'] += 1
        else:
            result = -1
            break
        idx += 1
    if result != -1:
        print(f"#{tc+1} {13 - card['S']} {13 - card['D']} {13 - card['H']} {13 - card['C']}")
    else:
        print(f'#{tc+1} ERROR')