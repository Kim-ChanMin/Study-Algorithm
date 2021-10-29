'''
Programmers - 숫자 문자열과 영단어
Language : Python
'''

def solution(s):
    # 변환하기 위한 dictionary
    dic = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
           'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}

    for i in dic:
        if i in s:
            s = s.replace(i, dic[i])

    return int(s)