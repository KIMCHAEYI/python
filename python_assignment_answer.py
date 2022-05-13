'''
덕성여대 멋쟁이사자처럼 10기 1차 python study 세션
실전 문제 도전! 모범답안
2022.04.28(목)
작성자 : 유다영
'''

'''
1. 회문
앞으로 읽으나 뒤로 읽으나 동일한 문장을 말한다.
예를 들어서 "mom", "civic", "dad" 등이 회문의 예이다.
사용자로부터 문자열을 입력받고 회문인지를 검사하는 프로그램을 작성하세요.
'''
pal_input = input("문자열을 입력하세요: ")  # 사용자에게 문자열을 입력받는다.


def palindrome(pal_input):  # 회문인지 구별하는 함수
    if bool(pal_input == pal_input[::-1]):  # 만약 입력한 문자열이 회문이라면
        print("회문입니다.")  # 회문입니다. 출력
    else:  # 입력한 문자열이 회문이 아니라면
        print("회문이 아닙니다.")  # 회문이 아닙니다. 출력
    return


palindrome(pal_input)  # 함수 호출
print("-------------------------------------------------------------")  # 문제 구별

'''
2. mbti의 검사결과는 아래와 같이 16가지 유형이 있다.
'ISTJ'
'ISFJ'
'INFJ'
'INTJ'
'ISTP'
'ISFP'
'INFP'
'INTP'
'ESTP'
'ESFP'
'ENFP'
'ENTP'
'ESTJ'
'ESFJ'
'ENTJ'

이때, 200명의 mbti 검사결과를 random 하게 만드는 함수 작성(200명의 검사 결과는 list로 담는다)

hint)문자열을 랜덤하게 출력하는 코드
import random

hint = "ABCDEFGH"
random.choice(hint)
'''
import random

# mbti 는 총 16가지 유형, 이를 리스트에 담음
mbti_list = ['ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP', 'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ',
             'ESFJ', 'ENTJ']


# 200명의 검사결과를 랜덤하게 만드는 함수

def random_mbti(mbti_result):
    # 리스트에서 랜덤으로 다수의 값 추출하기
    mbti_result += [random.choice(mbti_list) for i in range(0, 200)]
    # 200명의 검사결과가 잘 담기는지 확인
    print(len(mbti_result))
    # 200명의 각각의 검사결과 반환
    return mbti_result


# 검사결과를 담을 result 변수
mbti_result = []
# 함수 호출 및 출력
print(random_mbti(mbti_result))
print("-------------------------------------------------------------")  # 문제 구별

'''
3. 200명의 검사 결과가 각 16가지의 유형별 몇 명이 있는지 구하기
출력조건: 딕셔너리 형식( {'mbti유형': 총 명수})
출력예시: {'ESFP':17, 'INFJ': 13...}
힌트) 각각의 mbti 유형을 세는 법(counting)을 생각해보자.
'''
# 중복 요소를 카운팅한 결과를 담을 딕셔너리
mbti_count = {}

# for문와 try-except를 이용한 list안에 모든 요소들의 중복횟수 세기
for i in mbti_result:  # 200명의 검사결과 정보가 담긴 result 리스트의 요소를 for문을 돌면서 하나씩 꺼낸다
    try:
        mbti_count[i] += 1  # 리스트를 for문을 통해 돌면서 count에 이미 해당 현재 값의 요소가 있다면, try 문 실행 후 count 1 증가
    except:
        mbti_count[i] = 1  # count에 없는 key값이라면 except가 실행되며 값이 그냥 1로 저장

print(mbti_count)  # 딕셔너리 출력
print("-------------------------------------------------------------")  # 문제 구별

'''
4. mbti 유형을 딕셔너리의 key로 입력했을 경우, value로 몇 명이 해당 mbti에 속해있는지 출력하는 함수를 작성
추가 조건) 알파벳 입력시 대,소문자는 결과에 영향을 미치지 않도록 코드를 작성할 것 
'''
mbti_input = input("mbti 입력 하세요: ").upper()  # 사용자에게 mbti를 입력받은 걸 대문자로 바꿔 mbti_input이라는 변수에 저장
print(mbti_count.get(mbti_input))  # 해당 mbti에 몇명이 속해있는지 보여준다.
print("-------------------------------------------------------------")  # 문제 구별

'''
 5. 누구의 말을 들을까?
 
 1992년 멋사는 300만원을 가지고 있었다.
 친구 A는 은행에 돈을 맡겨 매년 이자로 8.5%씩 받는 것을 추천하였고,
 친구 B는 매매가 300만원인 한정판 시계를 구매하라고 추천하였다.
 2022년 기준 한정판 시계의 가격은 3500만원이 되었고, 1992년 은행에 300만원을 넣었을 경우 2022년에는 얼마가 있을지 계산하여 친구 A와 친구 B 중 누구의 말을 듣는 것이 이득이었을지 판단해보자
 
추가 조건) 상수와 변수의 정의를 이용해 작성해 볼 것 
출력 예시) "? 원 차이로 친구 ?가 맞았습니다."
'''

MONEY = 3000000  # 원금
R = 0.085  # 이자율
WATCH = 35000000  # 한정판 시계 가격

def benefit(money):
    suma=0
    for i in range(1992, 2022):  # 1992년부터 2022년까지의 이자율 계산
        MONEY *= (1 + R)
        print(MONEY)
    

    if MONEY > WATCH:
        print(f"{MONEY - WATCH}원 차이로 친구 A가 맞았습니다.")
    else:
        print(f"{WATCH - MONEY}원 차이로 친구 B가 맞았습니다.")
    return

benefit(MONEY)  # 함수 호출

print("finish!")
input("")
