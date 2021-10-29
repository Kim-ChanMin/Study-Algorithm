'''
Programmers - 신규 아이디 추천
Language : Python
'''

def solution(new_id):
    answer = ''

    # 1. 소문자 치환
    new_id = new_id.lower()
    # 2.  소문자, 숫자, '-', '_', '.'를 제외한 모든 문자를 제거
    for i in new_id:
        if i.islower() or i.isdigit() or i in ['-', '_', '.']:
            answer += i
    # 3. '.'가 두번 이상인 경우 한개의 '.'로 치환
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4. '.'가 처음이나 끝에 위치한다면 제거
    if answer[0] == '.':
        if len(answer) >= 2:
            answer = answer[1:]
        else:
            answer = '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5. 빈 문자열일 경우 "a" 대입
    if answer == '':
        answer = 'a'
    # 6. 16자 이상일 경우 첫 15개 이후는 모두 제거/ 제거 이후 마지막이 '.'일 경우 '.'도 제거
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7. 2자 이하일 경우 마지막 문자를 길이가 3이 될 때까지 반복하기
    while len(answer) < 3:
        answer += answer[-1]

    return answer