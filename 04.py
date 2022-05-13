'''
4. mbti 유형을 딕셔너리의 key로 입력했을 경우, value로 몇 명이 해당 mbti에 속해있는지 출력하는 함수를 작성
출력 조건) 알파벳 입력시 대,소문자는 결과에 영향을 미치지 않도록 코드를 작성할 것 
'''


import random
import collections

mbti = ["ESFP", "ESFJ", "ESTJ", "ESTP", "ENTP", "ENTJ", "ENFP", "ENFJ", "INFJ", "INFP", "ISFP", "ISFJ", "INTP", "INTJ", "ISTJ", "ISTP"]

choicelist = [random.choice(mbti) for i in range(200)]

mbti_counter = collections.Counter(choicelist)
print(mbti_counter)

print("-")

key = input('MBTI 유형을 입력하세요. : ').upper()

print(mbti_counter.get(key))