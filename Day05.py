'''
# [산술 연산자]
# [예제 1]
print("{}".format(3+2))     #[+] : 두 값을 더한 결과를 반환 
print("{}".format(3-2))     #[-] : 두 값을 뺀 결과를 반환 
print("{}".format(3*2))     #[*] : 두 값을 곱한 결과를 반환 
print("{}".format(3/2))     #[/] : 두 값을 나눈 결과를 반환(실수 값) 
print("{}".format(3//2))    #[//] : 두 값을 나눈 결과의 몫 반환(정수 값) 
print("{}".format(3%2))     #[%] : 두 값은 나눈 결과의 나머지 반환 
print("{}".format(3**2))    #[**] : 거듭 제곱의 결과 반환

# [비교 연산자]
# [예제 2]
print("{}".format(3==2))    #[==] : 두 피 연산자 값을 비교하여 동일하면 True, 동일하지 않으면 False 
print("{}".format(3!=2))    #[!=] : 두 피 연산자 값을 비교하여 동일하지 않으면 True, 동일하면 False
print("{}".format(3>2))     #[>] : 두 피 연산자 값을 비교하여 왼쪽의 값이 크면 True, 그렇지 않으면 False 
print("{}".format(3<2))     #[<] : 두 피 연산자 값을 비교하여 왼쪽의 값이 작으면 True, 그렇지 않으면 False 
print("{}".format(3>=2))    #[>=] : 두 피 연산자 값을 비교하여 왼쪽의 값이 크거나 같으면 True, 그렇지 않으면 False 
print("{}".format(3<=2))    #[<=] : 두 피 연산자 값을 비교하여 왼쪽의 값이 작거나 같으면 True, 그렇지 않으면 False

# [논리 연산자]
# [예제 3]
print(0 and 0, ":", False and False)    #[and] : 두 피 연산자가 전부 True인 경 우에만 True (논리곱)
print(1 and 0, ":", True and False)
print(0 and 1, ":", False and True)
print(1 and 1, ":", True and True)

print(0 or 0, ":", False or False)    #[or] : 두 피 연산자가 전부 False인 경 우에만 False (논리합)
print(1 or 0, ":", True or False)
print(0 or 1, ":", False or True)
print(1 or 1, ":", True or True)

print("not : ",not 0, ":", not False)   #[not] : 오른쪽 피 연산자에 대한 부정
print("not : ",not 1, ":", not True)
print("not : ",not (0 or 0), ":", not (False or False))   
print("not : ",not (1 or 1), ":", not (True or  True))

# [*멤버 연산자*]
# [예제 4]
print(1 in (1, 2, 3))   #[in] : 왼쪽 피 연산자의 값이 오른쪽 피 연산자 멤버 중 일치하는 값이 존재 하면 True 
print(1 not in (1, 2, 3))   #[not in] : 왼쪽 피 연산자의 값이 오른쪽 피 연산자 멤버 중 일치하는 값이 존재 하지 않으면 True
print(4 in (1, 2, 3))
print(4 not in (1, 2, 3))

# [식별 연산자]
# [예제 5]
num1, num2 = 1, '1' #num1 값은 정수형, num2 값은 문자형
print("{}".format(type(num1) is int))  #[is] : 두 피 연산자의 식별 값을 비교하 였을 때 동일한 객체이면 True 
print("{}".format(type(num2) is int))   #[is not] : 두 피 연산자의 식별 값을 비교하 였을 때 동일한 객체이면 False
print("{}".format(type(num1) is not str))
print("{}".format(type(num2) is not str))

# [비트 연산자]
# [AND 연산]
# 0 1 1 [3의 2진수 값]
# 1 0 1 [5의 2진수 값]
# ----- (AND 연산)
# 0 0 1 [0 0 1의 10진수 값은 1]
# [OR 연산]
# 1 1 1 (OR 연산 값 7)
# [XOR 연산] : 같으면 0을 반환, 다르면 1을 반환
# 1 1 0 (XOR 연산 값 6)

# [예제 6]
num1, num2 = 3, 5
bit1 = num1 & num2  #[&] : 두 피 연산자의 and 비트 연산을 수행 한다. 
bit2 = num1 | num2  #[|] : 두 피 연산자의 or 비트 연산을 수행 한다. 
bit3 = num1 ^ num2  #[^] : 두 피 연산자의 xor 비트 연산을 수행 한다. 
print("bir1 =", bit1)
print("bir2 =", bit2)
print("bir3 =", bit3)

num3 = 10
print("{:b}".format(num3))  #2진수
print("{}".format(num3<<2)) #[<<] : 왼쪽 피 연산자의 비트를 왼쪽으로 2개 비트 이동 
print("{}".format(num3>>2)) #[>>] : 왼쪽 피 연산자의 비트를 오른쪽으로 2개 비트 이동
print("{:b}".format(num3<<2))   #1byte = 1bit, 0000 1010으로 저장 된 상태에서 좌측으로 두칸 이동 -> 0010 10 인데 8칸을 채워야 하기 때문에 0010 1000 -> 앞에 00을 제외하고 출력. 10진수 값으로는 40(32+8)
print("{:b}".format(num3>>2))   # 0000 1000 -> 0000 0010(10)은 우측으로 밀려나 삭제 됨.

# [if 문]
# : 조건식이 참일 경우 종속문장을 실행한다.
# : 참이 아닐 경우에는 종속문장을 실행하지 않는다.
# : if문은 중첩이 가능하다.
# : if문의 종속문장은 반드시 들여쓰기를 진행한다.

# [EX: 들여쓰기]
num1 = int(input("정수 1개 입력:"))
if num1 == 1 :
    print("num1변수 값은 1입니다.") #들여쓰기를 하지 않으면 if의 종속문인지 알 수 없다.
    #<---- 실선이 보이며 if옆에 +, - 로 조절 가능하다.

# [예제 1]
num1 = int(input("정수입력:"))
if num1 % 2 == 0:
    print("num1 변수의 값은 짝수")
    print("num1 변수의 값은 2의 배수")
if num1 % 2 ==1:
    print("num1 변수는 홀수")

# [예제 2]
print("1.easy game")
print("2.hard game")
print("3.exit")
su = int(input("번호를 선택하세요:"))
if su == 1:
    print("easy game start")
if su == 2:
    print("hard game start")
if su == 3:
    print("game exit")

# [예제 3]
num1 = int(input("정수 입력:"))
if num1 == 1:
    print("변수 num1의 값은 {}입니다.".format(num1))

num2 = int(input("정수 입력:"))
if num2 > 10:
    print("변수 num2의 값은 10보다 큽니다.".format(num1))

num3 = int(input("정수 입력:"))
if num3 <= 10:
    print("변수 num3의 값은 10보다 작거나 같습니다.".format(num1))

# [문제 1]
# 날짜를 입력받아 요일을 구하세요.
# 단, 1일은 무조건 월요일, 7일은 일요일, 8일은 다시 월요일
# 날짜를 입력받아 요일을 출력하도록 코드를 작성

day = int(input("날짜를 입력:"))
result = day % 7
if result == 1:
    print("월요일")
if result == 2:
    print("화요일")
if result == 3:
    print("수요일")
if result == 4:
    print("목요일")
if result == 5:
    print("금요일")
if result == 6:
    print("토요일")
if result == 0:
    print("일요일")
'''














