'''
Programmers - 키패드 누르기
Language : Python
'''

def solution(numbers, hand):
    answer = ''
    # 왼손 시작 위치 지정
    leftHand = '*'
    # 오른손 시작 위치 지정
    rightHand = '#'
    # 전화 키패드를 dictionary로 선언
    keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2),
              4: (1, 0), 5: (1, 1), 6: (1, 2),
              7: (2, 0), 8: (2, 1), 9: (2, 2),
              '*': (3, 0), 0: (3, 1), '#': (3, 2)}

    for num in numbers:
        # 왼손만 사용하는 경우
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            leftHand = num
        # 오른손만 사용하는 경우
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            rightHand = num
        # 가운데 열을 누를 손 결정
        else:
            curPos = keypad[num]
            leftPos = keypad[leftHand]
            rightPos = keypad[rightHand]
            # Manhattan Distance 이용해서 거리 계산
            leftDist = abs(curPos[0] - leftPos[0]) + abs(curPos[1] - leftPos[1])
            rightDist = abs(curPos[0] - rightPos[0]) + abs(curPos[1] - rightPos[1])

            if leftDist < rightDist:
                answer += 'L'
                leftHand = num
            elif leftDist > rightDist:
                answer += 'R'
                rightHand = num
            else:
                if hand == 'left':
                    answer += 'L'
                    leftHand = num
                else:
                    answer += 'R'
                    rightHand = num

    return answer