'''
# [문제.1]
userin = input("이름과 나이를 입력(공백 구분):")
name,age = userin.split(' ')
print("이름:{}, 나이:{}".format(name,age))

# [문제.2]
ex = input("수식을 입력(EX:5*5):")
if '+' in ex:
    num1, num2 = ex.split('+')
    num1 = int(num1.strip())
    num2 = int(num2.strip())
    print(num1+num2)
elif '-' in ex:
    num1, num2 = ex.split('-')
    num1 = int(num1.strip())
    num2 = int(num2.strip())
    print(num1-num2)
elif '*' in ex:
    num1, num2 = ex.split('*')
    num1 = int(num1.strip())
    num2 = int(num2.strip())
    print(num1*num2)
elif '/' in ex:
    num1, num2 = ex.split('/')
    num1 = int(num1.strip())
    num2 = int(num2.strip())
    print(num1/num2)

# [함수]
# : 소스 코드내에서 작은 프로그램 단위를 의미한다.
# : 함수를 사용 할 경우 프로그램의 모듈화를 가져와 유지 보수 및 운영이 자유롭다.
# : Python에서는 함수를 정의하기 위해 "Definition"을 줄인 "def"를 키워드로 사용한다.
# : def 함수이름() :
# :     수행코드
# :     수행코드

def func1(arg1, arg2, arg3) :
    print(arg1, arg2, arg3)
func1(1,2,3)  #func1(매개변수1, 매개변수2) , func1을 호출하면서 데이터 값 1과 2를 넘겨주겠다는 뜻
            #코드의 실행순서는 호출 -> 해당함수 -> 기능 읽기. func1 -> def func1 -> print 순
func1("test","func","arg")


def func2(arg1, arg2=2) :
    print(arg1, arg2)
func2(5)    #출력 값 :5, 2 -> 초기 값 지정 가능
            #인자 값이 없는 arg1은 반드시 설정해주고 arg2는 초기값 2로 설정되어 있기 때문에 안해줘도 결과값이 나온다.

def func3(arg1, arg2) :
    print(arg1, arg2)
func3(100, 200)
func3(arg2=100, arg1=200)   #직접 지정해서 매개변수 입력 가능

def func3(arg1=0, arg2=0, arg3=0, arg4=0) :
    print(arg1, arg2, arg3, arg4)
func3(arg1=100, arg4=200)

def func4(arg) :
    return arg * arg    # return 문에는 아무것도 쓰면 안됨(if문 같은건 가능) -> 실행 x
f = func4       # 함수명이 길 경우 짧은 이름으로 저장 가능
result = f(5)       # 실행순서 func4를 result에 대입한다. def func4에 매개변수값 5를 저장. return arg*arg = 25를 result에 저장. 이 후 print result
print(result)

def func5(arg):
    return arg**arg #제곱 // 5에 5승

lst = [func5, 2]
a = lst[0](5)   # a = func5(5)
print(a)

# 지역변수 : 한정 된 지역에서만 사용되는 변수, 함수 내부에서 사용되는 지역변수는 함수 내에서 선언
# 전역변수 : 프로그램 전체에서 사용되는 변수, 모든 코드에서 사용하는 전역변수는 함수 바깥쪽에서 선언

def func1():
    #a = 100 # func1의 지역변수 a
    print(a)    # 이 지역을 벗어날 경우 사라진다.
                # 들여쓰기(TAB) 한 변수는 지역변수
def func2():
    #a = 200 # fun2의 지역변수 a
    print(a)
a = 200 # 전역 변수(전역 변수를 줄일수록 프로그램 성능이 좋아진다.)
func1()
func2()

var = 2 # 전역 변수
def func1(arg):
    var = 1 # 지역 변수
    print(var, arg)
func1(var)

def func1():
    #global a # a를 전역변수로 사용 func2 출력 값도 123
    a = 123
    print(a)
def func2():
    print(a)
a = 200
func1()
func2()

# [Quiz 1] : 전역변수 -> 지역변수
num = 10
sum=0
def display():
    sumFunc()
    print("10까지의 합 :", sum)
def sumFunc():
    global sum
    for i in range(num+1):
        sum+=i
display()


def display():
    num = 10
    print("10까지의 합 :", sumFunc(num))

def sumFunc(num):
    sum = 0
    for i in range(num+1):
        sum+=i
    return sum  # 호출한 곳으로 리턴, print("10까지의 합 :", sumFunc(num))
display()


def cal(su1,op,su2):
    result = 0
    result = su1 + su2
    print(su1, '+',su2, '=', result)
su1, op, su2 = int(input("숫자:")),input("부호:"),int(input("숫자:"))
cal(su1,op,su2)

def cal(su1,op,su2):
    result = 0
    result = su1 + su2
    print("계산기 실행!")
    return result 
su1, op, su2 = int(input("숫자:")),input("부호:"),int(input("숫자:"))
result = cal(su1, op, su2)
print(su1,'+',su2,'=',result)
print("계산기 종료!")

# 1. programInfo() 함수를 만들어서 다음과 같은 정보가 표시 될 수 있도록 하시오. 
# Version : 1.x 
# Update Date : 2017-01-01 
# Author : Project Python 
def programinfo():
    print("Version : 1.x")
    print("Update Date : 2017-01-01")
    print("Author : Project Python")
programinfo()

# 2. number 인자를 사용하는 inc(number), dec(number) 함수를 만들어 
# 함수로 전달한 number 값에 대해 inc 함수는 +1 증가, 
# dec함수는 -1 감소한 값을 출력하게 하시오. 
def inc(number):
    print(number + 1)
def dec(number):
    print(number - 1)
inc(10)
dec(10)

# 3. 위의 문제에서 값을 출력하지 말고 반환 할 수 있도록 하시오.
def inc(number):
    return number + 1
def dec(number):
    return number - 1
print(inc(10))
print(dec(10))


# 4. number 인자를 사용하는 rangeRand(number) 함수를 만들어 
# number 값에 따라 0 ~ number 까지 랜덤 값을 반환 하도록 하시오. 
from random import random
def rangeRand(number):
    return int(random() * (number + 1))
print(rangeRand(20))


# 5. start, end 인자를 사용하는 rangeRand(start, end) 함수 를 만들고 
# start ~ end 까지 랜덤 값을 반환 하도록 하시오.
from random import random
def rangeRand(start,end):
    if start >= end:
        return -1
    return start + int(random() * (end - start + 1))
print(rangeRand(10,20))
'''






