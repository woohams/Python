'''
import os
money , j = 0, 0
money = int(input("요금 투입:"))
while True:
    print("===============================================================")
    print("1.커피(200)\t2.코코아(250)\t\t3.반환\t\t4.종료")
    j = int(input("메뉴를 선택하세요 >>> "))
    if j == 4:
        break
    elif ((j == 1 and money < 200)or(j==2 and money < 250)):
        print("요금이 부족합니다.")
        os.system("pause")
        os.system("cls")
    elif j == 1:
        print("커피 맛있게 드세요."); money -= 200
        os.system("pause")
        os.system("cls")
    elif j == 2:
        print("코코아 맛있게 드세요."); money -=250
        os.system("pause")
        os.system("cls")  
    elif j == 3:
        print("반환금액: {}".format(money)); money = 0
        os.system("pause")
        os.system("cls")
    else:
        print("잘 못 입력")
        os.system("pause")
        os.system("cls")
print("프로그램 종료")
'''

# [Random 함수]
# : 코드를 작성하다가, 정해져 있지 않은 임의의 값을 생성할 때 사용한다.
# : 기본적인 random 함수만을 사용 할 경우 0.0 ~ 1.0 까지의 Random 값이 생성 된다.
# : Random 값의 범위는 조정 가능, 정수형태로도 Random 값을 구할 수 있다.
# : from random import random # Lib에 포함 기능
'''
from random import random 
# 0.0 ~ 1.0 미만의 값을 생성
print(random())
# 0.0 ~ 10.0 미만의 값을 생성
# 범위 설정 공식 : random() * "n"
print(random() * 10)
# 0 ~ 10 미만의 값을 생성
print(int(random() * 10))
# 1 ~ 10까지 임의의 값을 생성
print(int(random() * 10) + 1)
# 1 ~ 45까지 임의의 값을 생성
print(int(random() * 45) + 1)

for x in range(6):
    print(int(random()*45)+1)
# 31 42 18 40 43 27

from random import random,randrange
print(randrange(2,100,2)) # 짝수 출력
print(randrange(1,100,2)) # 홀수 출력

# 문제.1
from random import random
for i in range(0,6,1):
    print(int(random()*100)+1,end=" ")
print()

# 문제.2
from random import random
while True:
    rand = int(random()*100)+1
    print(rand)
    if rand == 50:  
        break

# 문제.3
from random import random
num1,num2,num3 = 0,0,0
while True:
    rand = int(random()*15)+1
    if rand != num1:
        num1 = rand
        break
while True:
    rand = int(random()*15)+1
    if rand != num1 != num2:
        num2 = rand
        break
while True:
    rand = int(random()*15)+1
    if rand != num1 != num2 != num3:
        num3 = rand
        break
print(num1,num2,num3)

# [List 자료형]
# : 리스트는 데이터의 목록을 다루는 자료형
# : 리스트를 정의할때에는 "[]"를 사용
# : 리스트 안에는 어떠한 형태의 데이터든지 저장 하여 사용 할 수 있다

# [예제.1]
lst = [1,2,3]
print(lst)
print(lst[0])
print(lst[1])
print(lst[2])

# [예제.2]
lst2 = [1,"서울",1.123]
print(lst2)
print(lst2[0])
print(lst2[1])
print(lst2[2])

# [예제.3]
lst3 = [1,2,3]
for idx in range(3):
    print(lst3[idx])

# [예제.4]
lst4 = [1,2,3,4,5,6,7,8,9,10]
for idx in range(len(lst4)):
    print(lst4[idx])

# [예제.5] ★
lst5 = ["test","python","list"] 
for value in lst5:
    print(value)


# [예제.6] 
a,b,c,d = 0,0,0,0
sum = 0
a = int(input("첫 번째 숫자 입력:"))
b = int(input("두 번째 숫자 입력:"))
c = int(input("세 번째 숫자 입력:"))
d = ("합계")
sum = a + b + c
print("{} : {}".format(d,sum))

a = [0,0,0,"합계"]
sum = 0
a[0] = int(input("첫 번째 숫자 입력:"))
a[1] = int(input("두 번째 숫자 입력:"))
a[2] = int(input("세 번째 숫자 입력:"))
sum = a[0] + a[1] + a[2]
print("{} : {}".format(a[3],sum))

a = [0,0,0,"합계"]
sum = 0
for i in range(len(a)-1):
	a[i] = int(input("정수 입력:")) 
sum = a[0] + a[1] + a[2]
print("{} : {}".format(a[3],sum))

'''






