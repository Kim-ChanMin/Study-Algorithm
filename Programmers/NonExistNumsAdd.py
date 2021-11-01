'''
Programmers - 없는 숫자 더하기
Language : Python
'''

def solution(numbers):
    answer = 0
    # 0~9까지의 합에서 numbers의 합을 빼기
    answer = 45 - sum(numbers)

    return answer