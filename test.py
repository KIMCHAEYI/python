import random
import collections

mbti = ["ESFP", "ESFJ", "ESTJ", "ESTP", "ENTP", "ENTJ", "ENFP", "ENFJ", "INFJ", "INFP", "ISFP", "ISFJ", "INTP", "INTJ", "ISTJ", "ISTP"]

choicelist = [random.choice(mbti) for i in range(200)]

mbti_counter = collections.Counter(choicelist)
print(mbti_counter)

print("-")

mbti = ["ESFP", "ESFJ", "ESTJ", "ESTP", "ENTP", "ENTJ", "ENFP", "ENFJ", "INFJ", "INFP", "ISFP", "ISFJ", "INTP", "INTJ", "ISTJ", "ISTP"]

key = input('MBTI 유형을 입력하세요. : ').upper()

print(mbti_counter.get(key))