'''
# [문제 1]
# 1. numbers = [10, 20, 30, 40, 50, 60, 70] 
# 위 리스트의 모든 값을 더한 결과를 출력 하시오
numbers = [10, 20, 30, 40, 50, 60, 70]
sum = 0
for i in range(len(numbers)):
    sum += numbers[i]
print(sum)

# [문제 2]
# 1 ~ 45 까지 임의의 값을 중복 없이 6개 생성하여 출력하는 코드를 작성 하시오
from random import random
numbers = []
cnt = 0
while True:
    rand = (int(random()*45)+1)
    if rand not in numbers:
        numbers.append(rand)
        cnt += 1
        if cnt==6:
            break
numbers.sort(reverse=False)
print(numbers)


# [문제 3]
# 3. lst_sec = [['홍길동', '남', 36], ['김수양', '여', 32], ['박담소', '남', 28]]
# 위의 2차 리스트 자료를 다음과 같은 형식으로 출력 하시오. 
# 이름 : 홍길동 성별 : 남 나이 : 36
lst_sec = [['홍길동', '남', 36],
           ['김수양', '여', 32],
           ['박담소', '남', 28]]

for value in lst_sec:
    print("이름 : {} ".format(value[0]),end='')
    print("성별 : {} ".format(value[1]),end='')
    print("나이 : {} ".format(value[2]),end='')
    print("\n")

# [문제 4]
# 4. 구구단을 출력하는 코드를 작성하되, 2차 리스트에 결과 값을 저장하고 출력 할 수 있도록 하시오.
# 형식 : 구구단 = [[2단],[3단],[4단],[5단],[6단],[7단],[8단],[9단]]
gugu = []
for x in range(1,10):
    gugu.append([])
    for y in range(1,10):
        gugu[x-1].append(x*y)

for x in range(2,10):
    for y in range(1,10):
        print("{} x {} = {}".format(x,y,gugu[x-1][y-1]))

# [Tuple]
# - 사전적 의미로는 n개의 요소로 이루어진 집합
# - List와 굉장히 유사한 구조를 갖는다.
# - List와 차이점
# - 1. 정의 형식 : List = [], Tuple = ()
# - 2. List는 자유롭게 데이터 변경 가능, Tuple 데이터 변경 불가능   a = list(1,2,3) : 튜플을 list로 변경
# - 3. List가 일반 데이터를 다루는데 주로 사용
# - 4. Tuple은 변경되지 않고, 오염이 없어야 하는 데이터를 다루는데 주로 사용
# - Ex: 위경도 좌표, RGB 색상표, 주소처리

tu = (1,2,3,4,5)
print(tu)
print(type(tu))
print(type(tu[0]))
print(len(tu))

print(tu[0])
print(tu[-1])
print(tu[0:3])
print(tu[2:5])

# tu[0] = 100 : 값 변경 불가능

# [예제 2] 
tu = "문자열", 100,1.1111
print(tu)
print(tu[0])
print(tu[1])
print(tu[2])
print(type(tu))
# 튜플은 ()가 생략 가능하다. 그러나 해주는게 좋다

tpint = (10)    # int
print(type(tpint))

tpT1 = (10,)    # tuple : ,를 찍어줘야 tuple형이 된다.
print(type(tpT1))

tpT2 = 20,  # tuple
print(type(tpT2))

# [예제 3] : tuple 합치기
a = 1,2,3
b = 4,5,6
c = a + b
print(a)
print(b)
print(c)
print(type(c))

# [예제 4] : packing, unpacking
pack = 1,2,"패킹"
print(pack)

a,b,c = pack # unpacking
print(a)
print(b)
print(c)

# [예제 5]
tu = (100,200,'함수',100,'개수')
print("tu안에 200의 위치:{}".format(tu.index(200)))
print("tu안에 100의 개수:{}".format(tu.count(100)))

# [Tuple 종합 문제]
# 1. 여러 개의 값을 패킹 시킨 후 저장되어 있는 값을 빼내어 출력하시오. (5개 값저장)
# (Tuple의 값을 리스트에 저장하시오. 단, Len 함수를 이용)
tp = (10, 20, "python", 1.123, "tuple")
ls = []
for i in range(len(tp)):
    ls.append(tp[i])
print(tp)
print(ls)

ls2 = list(tp)
print(ls2)
'''
# 2. 아래와 같이 출력 시키시오
# -------------------------------------------------------
#    (Tuple)        (List)
#    회사정보   :    삼성전자
#    제품명     :    Galaxy
#    가격정보   :    100원
#    출시일     :    미정
# -------------------------------------------------------
Tuple = ('회사정보', '제품명', '가격정보', '출시일')
List = ['삼성전자', 'Galaxy', '100원', '미정']
print("-------------------------------------------------------")
print("(Tuple)\t\t (List)")
for x in range(len(Tuple)):
    print("{:5}\t:{}".format(Tuple[x], List[x]))
print("-------------------------------------------------------")

# 3. 위에서 출력 한 내용을 업데이트 하시오.
# [단, Index, Insert, Remove 함수를 전부 사용할 것]
# 가격 : 100 -> 110
# 출시일 : 미정 -> 이번 달 말

tu = ("회사정보","제품명","가격정보","출시일")
ls = ["삼성전자","Galaxy","100원","미정"]
a = ls.index("100원")
b = ls.index("미정")
ls.remove("100원")
ls.remove("미정")
ls.insert(a,"110원")
ls.insert(b,"이번달말")
print("===============================================")
print("(Tuple)\t\t(List)")
for i in range(len(tu)):
    print("{:5}\t:{}".format(tu[i],ls[i]))
    