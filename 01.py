'''
1. 회문
앞으로 읽으나 뒤로 읽으나 동일한 문장을 말한다.
예를 들어서 "mom", "civic", "dad" 등이 회문의 예이다.
사용자로부터 문자열을 입력받고 회문인지를 검사하는 프로그램을 작성하세요.

힌트) 파이썬에서 문자열을 조작하는 방법은?
'''


word = input('문자열을 입력하세요 : ')
 
print(word == word[::-1])