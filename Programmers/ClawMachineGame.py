'''
Programmers - 크레인 인형뽑기 게임
Language : Python
'''

def solution(board, moves):
    # 인형을 담을 list
    picked = [0]
    answer = 0

    for i in moves:
        for j in board:
            if j[i - 1] != 0:
                # moved의 마지막에 같은게 들어있지 않으면 picked에 추가하기
                if picked[-1] != j[i - 1]:
                    picked.append(j[i - 1])
                    # 같은게 들어있으면 answer 추가하고 인형 없애기
                else:
                    answer += 2
                    picked.pop(-1)
                # 뽑았으므로 0으로 만들어주기
                j[i - 1] = 0
                break

    return answer