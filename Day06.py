'''
#[예제.1]
x = 15
if type(x) is int:
    print("x변수는 Int형 자료형")

#[예제.2]
x = 20
if x > 10 and x != 15:
    print("x는 10보다 크고 15와 같지 않습니다.")

# [예제 3]
x = 20
if x > 10 and x !=15:
    print("x는 10보다 크고 15와 같지 않습니다.")
else:
    print("x는 10보다 크고 15와 같습니다.")

# [예제 4]
num1 = 10
if num1 % 2 == 0:
    print("짝수이며, 2의배수!  ")
else:
    print("홀수")

# [if문 문제]
# 1. 입력한 데이터가 3의 배수인 경우 출력하시오.
su = int(input("데이터 입력:"))
if su % 3 == 0:
    print("데이터는 3의 배수")

# 2. 절대값을 구하는 프로그램을 작성하시오.
su = int(input("데이터 입력:"))
if su > 0:
    print(su)
else:
    print(-su)

# 3. 수를 입력 받아 짝, 홀수를 구분하여 출력하시오.
su = int(input("수를 입력:"))
if su % 2 == 0:
    print("데이터는 짝수")
else:
    print("데이터는 홀수")

# 4. 두 수를 입력받아 큰 수를 출력하시오.
su1 = int(input("첫번째 수를 입력:"))
su2 = int(input("두번째 수를 입력:"))
if su1 > su2:
    print(su1)
elif su1 < su2:
    print(su2)
else:
    print("같은 수")

# 5. 세 수를 입력받아 큰 수를 출력하시오.
su1 = int(input("첫번째 수를 입력:"))
su2 = int(input("두번째 수를 입력:"))
su3 = int(input("세번째 수를 입력:"))
if su1 > su2:
    if su1 > su3:
        print(su1)
if su2> su1:
    if su2 > su3:
        print(su2)
if su3 > su1:
    if su3 > su2:
        print(su3)

# 6. 두 수를 입력받아 큰 수가 짝수이면 출력하시오.
su1 = int(input("첫번째 수를 입력:"))
su2 = int(input("두번째 수를 입력:"))
if su1 > su2 and su1 % 2 == 0:
    print(su1)
elif su1 < su2 and su2 % 2 == 0:
    print(su2)

# 7. 두 수를 입력받아 합이 짝수이고 3의 배수인 수를 출력하시오.
su1 = int(input("첫번째 수를 입력:"))
su2 = int(input("두번째 수를 입력:"))
sum = su1 + su2
sum = int(sum)
if sum % 2 == 0 and sum % 3 == 0:
    print(sum)

# [예제 5] : 중첩 if문의 사용
num1 = int(input("정수입력:"))
if num1 % 2 == 0:
    if num1 % 3 == 0:
        print("3의 배수이며 짝수")
    else: #짝수이지만 3의 배수가 아닌 수
        print("짝수이지만, 3의배수가 아닙니다.")
else:
    print("짝수가 아닙니다.")

# [예제 6] : elif문의 사용(else if문)
num = int(input("정수입력(1~4):"))
if num == 1:
    print("1 입력")
elif num == 2:
    print("2 입력")
elif num == 3:
    print("3 입력")
elif num == 4:
    print("4 입력")
else:
    print("1, 2, 3, 4를 제외한 다른 수 입력")

# [문제 1]
# 1. 사용자로부터 이름, 키, 체중 값을 입력 받아 비만도를 구하고 
# 결과를 출력 할 때 비만도 값 100을 기준으로 100 미만이면 저체 중, 
# 100 이상 110 미만은 정상, 110 이상 120 미만 과제중, 120 이상 130 미만 비만, 
# 130 이상은 고도비만으로 출력 하시오.
# 비만도 계산 식 : 비만도(%) = 현재 체중 / 표준 체중 * 100 
# 표준 체중 계산 식 : 표준 체중 = (현재 키 – 100) * 0.9 
# 출력 예제 : 홍길동님의 비만도는 112.15% 로 과체중 입니다. 
name = str(input("이름 입력:"))
high = float(input("키 입력:"))
weight = float(input("몸무게 입력:"))
normweight = (high - 100) * 0.9
overweight = weight / normweight * 100
if overweight >= 100 and overweight < 110:
    print("{}님의 비만도는 {:.2f}%로 정상입니다.".format(name, overweight))
elif overweight >= 110 and overweight < 120:
    print("{}님의 비만도는 {:.2f}%로 과체중 입니다.".format(name, overweight))
elif overweight >= 120 and overweight < 130:
    print("{}님의 비만도는 {:.2f}%로 비만 입니다.".format(name, overweight))
elif overweight >= 130:
    print("{}님의 비만도는 {:.2f}%로 과체중 입니다.".format(name, overweight))

# [문제 2]
# turtle을 사용하여 3 ~ 10 까지의 값을 입력 받아 
# 삼각형 부터 십각형까지 그릴 수 있는 코드를 작성하시오.
# (위 입력 값의 범위 를 초과하는 경우 “그릴 수 없습니다.” 라는 메시지를 출력) 
import turtle
angle = int(input("수를 입력(3~10):"))
if angle == 3:
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.mainloop()
elif angle == 4:
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.mainloop()
elif angle == 5:
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.mainloop()
elif angle == 6:
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.mainloop()
elif angle == 7:
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.mainloop()
elif angle == 8:
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.mainloop()
elif angle == 9:
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.mainloop()
elif angle == 10:
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.forward(100)
    turtle.left(360 / angle)
    turtle.mainloop()
else:
    print("출력할 수 없습니다.")

# [문제 3]
# 윤년을 구하는 코드를 작성 하시오. 
# - 4의 배수는 윤년이 된다. 그 외는 평년 
# - 4의 배수 면서 100의 배수인 경우는 평년이다. 그 외는 윤년 
# - 4 그리고 100의 배수이면서 400의 배수인 경우 윤년이다. 그 외는 평년
year = int(input("년도를 입력하시오:"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "윤년입니다.")
        else:
            print(year, "평년입니다.")
    else:
        print(year, "윤년입니다.")
else:
    print("평년입니다.")

# [문제 4]
# 이름, 학번, 3과목의  성적을 입력 받아 합계와 평균을 구하고
# 평균이 90이상이면 'A', 80이상이면 'B', 70이상 'C', 60이상 'D', 60미만이면 'F'를 출력하시오.
name = str(input("이름을 입력하시오:"))
number = int(input("학번을 입력하시오:"))
sco1 = int(input("성적1을 입력하시오:"))
sco2 = int(input("성적2을 입력하시오:"))
sco3 = int(input("성적3을 입력하시오:"))
avg = (sco1 + sco2 + sco3) / 3
if avg >= 90:
    print("성적:A")
elif avg >= 80 and avg <90:
    print("성적:B")
elif avg >= 70 and avg <80:
    print("성적:C")
elif avg >= 60 and avg <70:
    print("성적:D")
elif avg < 60:
    print("성적:F")

# [문제 5]
# 커피의 개당 가격은 2000원이다. 10개 초과하면 초과하는 양에 대해서만 개당 1500원씩 받는다.
# 커피의 개수를 입력받아 금액을 출력하시오.
su = int(input("커피의 개수를 입력하시오:"))
price = 2000
if su <= 10:
    print("{}잔의 커피값은 {}원 입니다.".format(su, su*price))
elif su > 10:
    print("{}잔의 커피값은 {}원 입니다.".format(su, 20000 + (su-10) * (price - 500)))

# [문제 6]
# 정수를 입력받아 아래와 같이 출력하시오.
# 3의 배수이면서, 4의 배수입니다.
# 3의 배수입니다.
# 4의 배수입니다.
# 3의 배수도, 4의 배수도 아닙니다.
# 0은 3의 배수도, 4의 배수도 아닙니다.
su = int(input("정수를 입력하시오:"))
if su % 3 == 0 and su % 4 == 0:
    print(su,"는 3의 배수이면서, 4의 배수입니다.")
elif su % 3 == 0:
    print(su,"는 3의 배수입니다.")
elif su % 4 == 0:
    print(su,"는 4의 배수입니다.")
elif su % 3 == 1 or 2 and su % 4 == 1 or 2 or 3:
    print(su,"는 3의 배수도, 4의 배수도 아닙니다.")
elif su == 0:
    print(su,"은 3의 배수도, 4의 배수도 아닙니다.") #여러개의 조건을 만족시키는 것들을 윗쪽으로 배치해야 효과적인 코드
'''
# [문제 7]
# 비행기를 타는데 30분 거리까지의 기본 요금은 300000원 이며,
# 10분 단위로 추가요금 5000원씩 부가된다.
# 비행기를 탈 시간을 입력하여 요금 계산기를 만드시오.
money = 30000
time = int(input("비행기를 탈 시간을 입력하시오:"))
time = time - 30
if time > 0:
    if time % 10 == 0:
        money = money + time // 10 * 5000 #(//는 소숫점을 제외한 정수만 나눗셈)
    else:
        money = money + time // 10 * 5000 + 5000 #1분 단위로 추가되도 5천원이 추가되야 하므로 +5000
print(money,"원 입니다")







