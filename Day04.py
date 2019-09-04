 # [Input]
 # - 데이터를 입력 받는 함수 (print 반대)
 # - 데이터를 입력 받을 경우 기본 값 ★"문자열"★ 로 인식(정수, 실수 값을 입력하려면 명시를 해줘야 됨)
 # - 값을 입력받아 연산을 진행 할 경우 형 변환 하여 입력한다.(int, floot)
'''
 # [예제 1]
print("2개의 정수를 입력하세요.")
num1 = input("첫 번째 정수:")
num2 = input("두 번째 정수:")
num3 = num1 + num2
print(num3) #첫 번째 정수(10입력) + 두 번째 정수(10입력)를 합치면 1010이 나온다. - 이유 : 문자열로 인식하기 때문에 python에서는 문자열간에 계산이 가능해 1010이 나오는 것.

# 형 변환 방법 1
print("2개의 정수를 입력하세요.")
num1 = int(input("첫 번째 정수:"))
num2 = int(input("두 번째 정수:"))
num3 = num1 + num2  
print(num3)

# 형 변환 방법 2
print("2개의 정수를 입력하세요.")
num1 = input("첫 번째 정수:")
num2 = input("두 번째 정수:")
num3 = int(num1) + int(num2)
print("2개의 정수의 합은: ", num3)
print("num1 Type: {}".format(type(num1)))
print("num2 Type: {}".format(type(num2)))
print("num3 Type: {}".format(type(num3)))

# [문제 1]
# 출력 : 이름입력
# 입력 : 홍길동
# 출력 : 나이입력
# 입력 : 20
# 결과 : 홍길동 님의 나이는 20살 입니다.

print("이름과 나이를 입력하세요.")
name = input("이름입력:")
age = int(input("나이입력:"))
print("{}님의 나이는 {}살 입니다.".format(name, age))  

# [예제 2]
su1 = int(input("첫 번째 정수입력:"))
su2 = int(input("두 번째 정수입력:"))
result = su1 + su2
print("su1 + su2 = ", result)
result = su1 - su2
print("su1 - su2 = ", result)
result = su1 * su2
print("su1 * su2 = ", result)
result = su1 / su2
print("su1 / su2 = ", result)

# [문제 2]
# 학생 이름과 국어, 영어. 수학 점수를 입력 받아 출력하시요.
# 학생 이름 : 강사
# 국어 점수 : 1
# 영어 점수 : 2
# 수학 점수 : 2
# =================학생 정보=================
# 이름  국어    영어    수학    합계    평균
# 강사    1      2       2      5     1.67

print("학생 이름과 국어, 영어, 수학 점수를 입력 받아 출력하시오.")
name = (input("학생 이름 : "))
sco1 = int(input("국어 점수 : "))
sco2 = int(input("영어 점수 : "))
sco3 = int(input("수학 점수 : "))
sum = sco1 + sco2 + sco3
avg = sum / 3
print("=================학생 정보=================")
print("이름\t국어\t영어\t수학\t합계\t평균")
print("{}\t {}\t {}\t {}\t {}\t{:.2f}".format(name, sco1, sco2, sco3, sum, float(avg)))

# [문제 3]
# 3.1  input()으로 사용자 입력을 받고 이름과 나이를 출력하는 코드 를 작성하시오. 
# 출력 예제 : 홍길동님의 나이는 38세 입니다. 
print("이름과 나이를 입력하시오.")
name = (input("이름 입력:"))
age = int(input("나이 입력:"))
print("{}님의 나이는 {}세 입니다.".format(name, age))

# 3.2 input()으로 2개의 값을 받고 더하기, 빼기, 곱하기, 나누기 연산을 하여 
# 그 결과를 출력하는 코드를 작성하시오. 
su1 = int(input("첫 번째 값 입력:"))
su2 = int(input("두 번째 값 입력:"))
sum = su1 + su2
print("su1 + su2 = ", sum)
sub = su1 - su2
print("su1 - su2 = ", sub)
mul = su1 * su2
print("su1 * su2 = ", mul)
div = su1 / su2
print("su1 / su2 = ", div)

# 3.3 사용자로부터 이름, 키, 체중 값을 입력 받아 비만도를 구하고 
# 출력하는 코드를 작성하시오. 
# 비만도 계산 식 : 비만도(%) = 현재 체중 / 표준 체중 * 100 
# 표준 체중 계산 식 : 표준 체중 = (현재 키 – 100) * 0.9 
# 출력 예제 : 홍길동님의 비만도는 112.15% 입니다.

print("이름과 키, 체중 값을 입력하시오.")
name = (input("이름 입력:"))
high = float(input("키 입력:"))
weight = float(input("몸무게 입력:"))
표준체중 = (high - 100) * 0.9
비만도 = weight / 표준체중 * 100
print("{}님의 비만도는 {:.2f}% 입니다.".format(name, 비만도))

# [Turtle]
# 거북이 그래픽
# Turtle은 내장되어 있는 print, input과 달리 외장되어 있기때문에 호출해야지 사용이 가능하다.
# 외부모듈을 사용하기 위해 import를 사용한다.(호출, turtle의 경우 다운받을 필요 없이 호출만으로 가능)

import turtle
turtle.forward(90)  # 90만큼 앞으로 이동
turtle.left(120)    # 120도 만큼 좌회전
turtle.forward(90)
turtle.left(120)
turtle.forward(90)
turtle.left(120)
turtle.mainloop()   # 프로그램이 종료되지 않고 유지

# [문제 4]
# 1. input() 함수를 사용하여 한 변의 길이 값을 입력 받아 정삼각 형을 그리는 코드를 작성하시오. 
print("변의 길이를 입력하시오.")
side = int((input("변의 길이:")))
import turtle
turtle.forward(side)
turtle.left(120)
turtle.forward(side)
turtle.left(120)
turtle.forward(side)
turtle.left(120)
turtle.mainloop()

# 2. input() 함수를 사용하여 가로, 세로 길이 값을 입력 받아 사 각형을 그리는 코드를 작성하시오. 
print("가로, 세로의 길이를 입력하시오.")
side1 = int((input("가로의 길이:")))
side2 = int((input("세로의 길이:")))
import turtle
turtle.forward(side1)
turtle.right(90)
turtle.forward(side2)
turtle.right(90)
turtle.forward(side1)
turtle.right(90)
turtle.forward(side2)
turtle.right(90)
turtle.mainloop()
'''
# 3. input() 함수를 사용하여 한 변의 길이 값을 입력 받아 정육각 형을 그리는 코드를 작성하시오.
print("변의 길이를 입력하시오.")
side = int((input("변의 길이:")))
import turtle
turtle.forward(side)
turtle.left(60)
turtle.forward(side)
turtle.left(60)
turtle.forward(side)
turtle.left(60)
turtle.forward(side)
turtle.left(60)
turtle.forward(side)
turtle.left(60)
turtle.forward(side)
turtle.left(60)
turtle.mainloop()

# 산술연산자
# % : 두값을 나눈 결과의 나머지 (짝,홀수 구분가능 - 2로 나눴을 때 나누기 값이 0이면 짝, 1이면 홀)


