'''
Programmers - 로또의 최고 순위와 최저 순위
Language : Python
'''

def solution(lottos, win_nums):
    answer = []
    cnt_zero = lottos.count(0)
    cnt_win = 0

    # 맞춘 번호 count
    for i in win_nums:
        if i in lottos:
            cnt_win += 1

    # 모든 번호를 모를 경우
    if cnt_zero == 6:
        return [1, 6]

    # 모든 번호가 있지만 다 틀릴 경우
    elif cnt_zero == 0 and cnt_win == 0:
        return [6, 6]

    # 1~5위 성립
    answer.append(7 - (cnt_zero + cnt_win))
    answer.append(7 - cnt_win)

    return answer