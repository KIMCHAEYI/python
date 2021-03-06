'''
덕성여대 멋쟁이사자처럼 10기 1차 python study 세션
실전 문제 도전!

작성일: 2022.04.28(목)
'''

'''
1. 회문
앞으로 읽으나 뒤로 읽으나 동일한 문장을 말한다.
예를 들어서 "mom", "civic", "dad" 등이 회문의 예이다.
사용자로부터 문자열을 입력받고 회문인지를 검사하는 프로그램을 작성하세요.

힌트) 파이썬에서 문자열을 조작하는 방법은?
'''


word = input('문자열을 입력하세요 : ')
 
print(word == word[::-1])



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

이때, 200명의 mbti 검사결과를 random 하게 만드는 함수를 작성해보세요

출력 조건) 200명의 검사 결과는 list로 담는다
힌트) 문자열을 랜덤하게 출력하는 코드는 아래와 같습니다.
import random

hint = "ABCDEFGH"
random.choice(hint)
'''


import random

mbti = ["ESFP", "ESFJ", "ESTJ", "ESTP", "ENTP", "ENTJ", "ENFP", "ENFJ", "INFJ", "INFP", "ISFP", "ISFJ", "INTP", "INTJ", "ISTJ", "ISTP"]

choicelist = [random.choice(mbti) for i in range(200)]
print(choicelist)



'''
3. 200명의 검사 결과가 각 16가지의 유형별 몇 명이 있는지 구하기

출력 조건) 딕셔너리 형식( {'mbti유형': 총 명수})
출력 예시) {'ESFP':17, 'INFJ': 13...}
힌트) 각각의 mbti 유형을 세는 법(counting)을 생각해보자.
'''

import random
import collections

mbti = ["ESFP", "ESFJ", "ESTJ", "ESTP", "ENTP", "ENTJ", "ENFP", "ENFJ", "INFJ", "INFP", "ISFP", "ISFJ", "INTP", "INTJ", "ISTJ", "ISTP"]

choicelist = [random.choice(mbti) for i in range(200)]

mbti_counter = collections.Counter(choicelist)
print(mbti_counter)




'''
4. mbti 유형을 딕셔너리의 key로 입력했을 경우, value로 몇 명이 해당 mbti에 속해있는지 출력하는 함수를 작성
출력 조건) 알파벳 입력시 대,소문자는 결과에 영향을 미치지 않도록 코드를 작성할 것 
'''

import random
import collections

mbti = ["ESFP", "ESFJ", "ESTJ", "ESTP", "ENTP", "ENTJ", "ENFP", "ENFJ", "INFJ", "INFP", "ISFP", "ISFJ", "INTP", "INTJ", "ISTJ", "ISTP"]

key = input('MBTI 유형을 입력하세요. : ').upper()

choicelist = [random.choice(mbti) for i in range(200)]
mbti_counter = collections.Counter(choicelist)

print(mbti_counter.get(key))





'''
 5. 1992년 멋사는 300만원을 가지고 있었다.
 친구 A는 은행에 돈을 맡겨 매년 이자로 8.5%씩 받는 것을 추천하였고,
 친구 B는 매매가 300만원인 한정판 시계를 구매하라고 추천하였다.
 2022년 기준 한정판 시계의 가격은 3500만원이 되었고, 1992년 은행에 300만원을 넣었을 경우 2022년에는 얼마가 있을지 계산하여 친구 A와 친구 B 중 누구의 말을 듣는 것이 이득이었을지 판단해보자
 
추가 조건) 상수와 변수의 정의를 이용해 작성해볼 것 
출력 예시) "? 원 차이로 친구 ?가 맞았습니다."
'''

INTEREST_RATE = 0.085 
WATCH_PRICE = 35000000

capital = 3000000
year = 1992

while year < 2022:
    capital = capital * (1 + INTEREST_RATE)
    year += 1

if capital > WATCH_PRICE:
    print("{}원 차이로 친구A가 맞았습니다.".format(int(capital - WATCH_PRICE)))
else:
    print("{}원 차이로 친구B가 맞았습니다.".format(int(WATCH_PRICE - capital)))