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