'''
# 1. 짝, 홀수를 구분하는 함수를 작성해 주세요.

def evenOdd(num):
    if num % 2 ==0:
        return 0
    else:
        return 1


num = int(input("수 입력:"))
result = evenOdd(num)
if result ==0:
    print("입력 값: ", num, " 짝수")
else:
    print("입력 값: ",num," 홀수")


# 2. "3"의 배수를 판별하는 함수를 작성해 주세요.
def test(num):
    if num % 3 ==0:
        return 0
    else:
        return 1


num = int(input("수 입력:"))
result = test(num)
if result ==0:
    print("입력 값: ", num, " 3의 배수")
else:
    print("입력 값: ",num," 3의 배수가 아닙니다.")

# 3. 계산기를 입력,출력,연산기능으로 나눠서 실행되게 작성해 주세요.
def calc(su1, op, su2):
    if op == '+':
        result = su1 + su2
    elif op =='-':
        result = su1 - su2
    elif op == '*':
        result = su1 * su2
    elif op =='/':
        result = su1 / su2
    return result

def output(su1, op, su2, result):
    print(su1,op,su2,"=",result)

def inPut():
    su1 = int(input("숫자:"))
    op = input("부호:")
    su2 = int(input("숫자:"))
    result = calc(su1,op,su2)
    output(su1, op, su2, result)
inPut() #호출하면서 에러나서 대문자 P로 바꿈.

# 4. 거꾸로 수를 반환하는 함수를 계산,출력 기능으로 나눠서 작성해 주세요.
def reverseCode(result):
    temp,su = 0,0
    while True:
        temp = int(result%10)   # 나머지 값 저장
        result = int(result/10) # 몫 값 저장
        su = (su+temp)*10   # su 값에 계속 누적되어 저장
        if not result:
            return int(su/10)   # *10한 값 다시 /

def display():
    reulst,su = 0,0
    result = int(input("수 입력: "))
    su = reverseCode(result)
    print("반환 된 값: ",su)    #reverseCode에서 반환 된 값 출력

print("프로그램 시작")
display()
print("프로그램 종료")

# 5. 자판기를 선택,출력 기능으로 나눠서 함수화 하여 작성해 주세요.
def sel_machine(sel):
    result = ''
    if sel ==1: result = "콜라"
    elif sel ==2: result = "핫6"
    elif sel ==3: result = "포카리"
    else : return "존재하지 않는 음료입니다."
    if sel >=1 and sel <=3:
        return result + " 맛있게 드세요."

def display():
    sel = int(input("음료 선택\n1.콜라\n2.핫6\n3.포카리\n입력:"))
    result = sel_machine(sel)
    print(result)
display()


# a=10, b=20일 때 값을 교환하고 싶다면 tmp를 만들어 tmp=a, a=b, b=tmp로 교환알고리즘 생성

# def swap(x,y):
#   return y,x - 함수 사용하여 교환

#  람다 함수
# [예제 1]
swap = lambda a,b:[b,a] # 변수처럼 보이지만 함수 (def 생략개념)
a = swap(10,20)
print(a)

# [예제 2]
lam = lambda a: a*10
hap = lambda a,b: a+b
noData = lambda : print("인자 값 없는 람다")

print(lam(10))  #100
print(hap(5,10))    #15
noData()    #인자 값 없는 람다 - 3개의 함수 작성, lam,hap,noData는 함수명 / lambda가 인자 값 / : 뒤의 것이 함수 내용

# [문제 1]
# 1. 람다 함수를 이용하여 두 수의 +,-,*,/의 기능을 만들고 실행.
lam1 = lambda a,b: a+b
lam2 = lambda a,b: a-b
lam3 = lambda a,b: a*b
lam4 = lambda a,b: a/b

a = int(input("수1:"))
b = int(input("수2:"))
print("두 수의 합: ",lam1(a,b))
print("두 수의 차: ",lam2(a,b))
print("두 수의 곱: ",lam3(a,b))
print("두 수의 나눈 값: ",lam4(a,b))

# [문제 2]
# 2. 디폴트 매개변수를 이용한 요금 구하는 프로그램 만들기
#    기본요금 500원 환승이 없거나 환승 1회까지는 기본요금
#    1회를 초과하는 환승의 경우 환승 1회마다 요금의 2배씩 증가된다.
#    ( EX: 환승 2회일 경우 : 1000원, 환승 3회일 경우 : 2000원 )
#    장거리는 10000원으로 처리한다.
#    1. 환승 안함
#    2. 환승 함
#    3. 장거리

def transfer(dest, su=1, won=500):  #디폴트 매개변수 선언
    for i in range(1,su):
        won *= 2
    return "{}까지 요금 : {}원 입니다.".format(dest,won)    #return값은 result에 들어감

def display():
    dest = ''
    su = 0
    num = int(input("1.환승 안함\n2.환승 함\n3.장거리\n번호 입력:"))
    dest = input("목적지 입력: ")
    if num ==1:
        result = transfer(dest)
    elif num ==2:
        su = int(input("환승 수 입력:"))
        result = transfer(dest, su)
    else:
        result = transfer(dest, 1, 10000)
    print(result)
display()


# [Python 모듈 및 패키지 사용]
# 모듈 : 함수, 변수, 클래스 등을 모아놓은 파일 ("import")
# 모듈을 만드는 방법 : *.py --> import *.py 해서 사용 가능

# [예제 1] : 내장 모듈 사용
import datetime
import time

s = datetime.datetime.now()
print("s:", s)

t = time.localtime()
print("t:",t)
print("t.tm_year:",t.tm_year)

time1 = time.time()
print("time1:", time1)
time2 = time.time()
print("time2:",time2)

time.sleep(10)  #지연 값 설정(10초), sockat 프로그램 시 사용 多

time3 = time.time()
print("time3 - time2", int(time3 - time2),"초

'''
from packTest import *
print("sum",sum.sumFunc(10,2))
print("sub",sub.subFunc(10,2))
print("mul",mul.mulFunc(10,2))
print("div",div.divFunc(10,2))




