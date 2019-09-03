# [변수]
# : 한 가지의 값으로 고정되어 있지 않고, 여러 값으로 변할 수 있는 공간을 의미한다.  
# : 데이터를 사용하기 위해 메모리의 공간을 할당 받아 해당 공간에 이름을 부여하여 사용한다.

# [변수 작명 규칙]
# 1. 변수명은 알파벳, 숫자, 언더바("_")로 구성된다.
# 2. 대, 소문자를 구분해서 사용한다. (EX: test, Test는 다른 공간으로 구분)
# 3. 한글 사용이 가능하다. (EX: 테스트)
# 4. 공백이나 특수기호는 포함 될 수 없다.(띄어쓰기 불가)
# 5. Python 예약어는 변수 이름으로 사용이 불가능하다.

# [변수 자료형의 종류]
# 1. 정수(int) : 0가 음수, 양수 값을 포함하는 숫자 값
# 2. 실수(floot) : 소수점을 사용하는 숫자 값
# 3. 문자열(string) : 따옴표로 묶어 있는 문자 값
# 4. 리스트(list) : 정수, 실수 및 문자열 등 자료들의 집합 (값의 집합, 어떠한 값들의 묶음 단위)
# 5. 튜플(tuple) : 정수, 실수 및 문자열 등 자료들의 집합 (값의 집합, 어떠한 값들의 묶음 단위)   // 차이점은 나중에..
# 6. 사전(dictionary) : 정수, 실수 및 문자열 등 자료들의 집합 (키와 값이 쌍으로 존재)

# [변수 기본 사용]
# 1. 변수명 = 값
# 2. 변수명1, 변수명2 = 값1, 값2
# 3. 변수명1 = 변수명2 = 값 (값이 변수명2의 대입, 변수명2의 값이 변수명1에 대입)
# = : 오른쪽에 있는 것을 왼쪽에 대입하는 기호
# == : 같다(수학적 의미의 =)

'''
# [예제 1] - 변수 선언
var1 = 1  #일반 변수 선언
var2, var3 = 2, 3  #여러개의 변수 동시 선언
var4 = var5 = 4  #여러개의 변수에 값 대입
print("var1={}, var2={}, var3={}, var4={}, var5={}".format(var1, var2, var3, var4, var5))

var1 = 10; var2 = 20; var3 = 30; var4 = 40 ;var5 = 50  #변수 값 변경, 원한다면 언제든지 변수 값 변경 가능
print("var1={}, var2={}, var3={}, var4={}, var5={}".format(var1, var2, var3, var4, var5))
'
# [예제 2] - type함수 사용
var1, var2, var3 = "Test", 1, 1.123
print("var1 = {}, var1 Type = {}".format(var1, type(var1)))
print("var2 = {}, var2 Type = {}".format(var2, type(var2)))
print("var3 = {}, var3 Type = {}".format(var3, type(var3)))

# type함수는 변수의 자료형을 확인하기 위해 사용된다.

# [예제 3]
var1, var2, var3 = "1", 1, 1.0
var1, var2, var3 = int(var1), float(var2), str(var3)    # int(var1) - 문자열이었던 var1의 값 1을 int형으로 변경시켰다.
                                                        # 마찬가지로 var2의 int형을 float형으로, var3의 float형을 str형으로 변경시켰다.
print("{}".format(type(var1)))
print("{}".format(type(var2)))
print("{}".format(type(var3)))

num = 5
print("Num 변수의 변경 전 데이터:{}".format(num))
print("Num 변수의 변경 전 자료형:{}".format(type(num)))
num = num + 10
num = str(num)  #int 형이었던 num을 강제로 str형으로 변경시킨다.
print("Num 변수의 변경 후 데이터:{}".format(num))
print("Num 변수의 변경 후 자료형:{}".format(type(num)))

# [예제 4]
num1 = 5
num2 = 10
sum = num1 + num2
print("num1 = {}".format(num1))
print("num2 = {}".format(num2))
print("두 변수의 합은 = {}".format(sum))


# [문제 1] : num1(10) + num2(20) = 30 출력해주세요.
# 단, 10, 20, 30은 변수를 이용하여 출력
num1 = 10
num2 = 20
sum = num1 + num2
print("num1({}) + num2({}) = {}".format(num1, num2, sum))

# [문제 2]
# num1 = 7
# num2 = 5
# 위 값의 연산 결과를 각각의 변수에 저장 후 출력 (+, -, *, /)
num1 = 7
num2 = 5
sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
print("num1 + num2 = {}".format(sum))
print("num1 - num2 = {}".format(sub))
print("num1 * num2 = {}".format(mul))
print("num1 / num2 = {}".format(div))

# [문제 3]
# 1. 다음과 같이 나오도록 코딩하세요. (단, 변수를 사용할 것) Python 100점 !!!
# 2. 다음과 같이 나오도록 코딩하세요. (단, 변수를 사용할 것) 나는 20살입니다. ^^!
# 3. Python, C언어, Java 3과목의 점수를 각 변수에 저장
# 합계와 평균을 구하는 프로그램을 만드시오.(평균은 소수점 2자리 까지)

sco1 = 100
age1 = 20
sco2 = 90
sco3 = 80
print("Python {}점 !!!".format(sco1))
print("나는 {}살 입니다.".format(age1))
print("Python 점수 : {}, C언어 점수 : {}, Java 점수 : {}".format(sco1, sco2, sco3))

sum = sco1 + sco2 + sco3
avg = sum / 3
print("세 과목의 합계는 {}".format(sum))
print("세 과목의 평균 점수는 {:.2f}".format(avg))
'''
# [문제 4]
#su = 100; num= "100"; fit=1.111
# 위 변수들을 이용하여 아래와 같은 출력 결과가 나오도록 코드를 완성해주세요.
# 200
# 101.111
# 100100

su = 100; num ="100"; fit=1.111
print("정수 형변환: {}".format(su+int(num)))
print("실수 형변환: {}".format(su+fit))
print("문자열 형변환: {}".format(str(su)+num))  #다른 언어와 달리 문자열끼리 계산이 가능함(100+100이 더해져서 결과 값 100100이 됨)

# [문제 5]
# 당신은 놀이공원을 가기 위해 11개의 지하철 역을 지나왔다.
# 출발 역에서 도착역까지 37분이 걸렸다면 한 역을 지나는데 걸리는 시간은 얼마인가? (소수점 2자리까지)

sub = 11
min = 37
avg = min / sub
print("당신이 한 역을 지나는데 걸린 시간은 {:.2f}분이다.".format(avg))

# [문제 6]
# 호텔 한 층의 높이는 260cm이다. 총 14개의 층을 쓰고 있으며
# 1층은 500.23cm라면 이 건물의 높이는 총 몇 m인가? (단, 소수점 3자리까지)

flohigh = 260
flo = 13
flo1 = 500.23
high = flohigh * flo + flo1
print("이 건물의 높이는 총 {:.3f}m이다".format(high / 100))


# [문제 7]
# 전동 자전거로 100m를 가는데 11.27초가 걸린다면 1시간 후 몇 km를 갈 수 있을까? (소수점 2자리까지)
# 시간단위를 초단위로 변경, 바뀐 초값을 11.27초로 나눈 후 x100을 하면 m값이 나옴. 그것을 km 단위로 바꾸면 됨
m = 3600 / 11.27 * 100
print("1시간 후 간 거리는 {:.2f}km이다".format(m / 1000))


