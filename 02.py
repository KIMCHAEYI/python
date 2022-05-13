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