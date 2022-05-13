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