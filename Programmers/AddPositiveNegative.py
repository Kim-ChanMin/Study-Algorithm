'''
Programmers - 음양 더하기
Language : Python
'''

def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        # 양수인 경우
        if signs[i] == True:
            answer += absolutes[i]
        # 음수인 경우
        else:
            answer -= absolutes[i]

    return answer