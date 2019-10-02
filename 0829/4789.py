# 성공적인 공연 기획
T = int(input())
for tc in range(T):
    string = input() # 첫번째 글자 기립 박수하는 사람 수
    active_people = int(string[0])

    idx = 1
    buy = 0
    for i in string[1:]:
        if idx <= active_people:
            active_people += int(i)
        else:
            buy += idx - active_people
            active_people += int(i) + idx - active_people
        idx += 1

    print('#{} {}'.format(tc+1, buy))