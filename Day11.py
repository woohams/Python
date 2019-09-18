'''
lst = [1, 2, 3]
print(lst)
print(lst[-1])  # 뒤에서부터 -1, 출력 값:3
print(lst[-3])  # 뒤에서부터 -3, 출력 값:1
print(lst[0:-1])

#[예제 1] : list 음수값으로 첨자 표현
a = [0, 0, 0, "합계"]
sum = 0
for i in range(-4, -1, 1):  #-4에서 1 증가하면 -3
    a[i] = int(input("정수 입력:"))
sum = a[-4] + a[-3] + a[-2]
print("{}:{}".format(a[-1], sum))

#슬라이싱
#      [1, 2, 3, 4, 5, 6]
#접근: 0  1  2  3  4  5   - 중간중간에 들어간다는 개념
#음수:-6 -5 -4 -3 -2 -1

#[예제 2] : list 슬라이싱 표현
lst = [10, 20, 30, 40, 50]
print("list[1:3]={}".format(lst[1:3]))  # 1부터 3까지 - 20, 30
print("list[0:3]={}".format(lst[0:3]))  # 0부터 3까지 - 10, 20, 30
print("list[3:]={}".format(lst[3:]))    # 3 다음부터 - 40, 50
print("list[:3]={}".format(lst[:3]))    # 3까지 - 10, 20, 30

#[list 복사]
# 얇은복사, 깊은복사 2가지의 형태가 존재한다.
# 얇은복사는 원본 리스트의 주소값을 사본 리스트에 적용(ex: 바로가기(링크개념))
# 얇은복사는 쉽게 원본 리스트의 또 다른 이름이 부여되는 것
# ex: Lst1 = [1, 2, 3]
#     Lst2 = Lst1
# 깊은 복사는 원본 리스트에 데이터값을 실제 복사하여 새로운 사본리스트에 저장
# 일반적으로 우리가 문서편집시 사용하는 복사의 형태
# 단, 반드시 import copy 모듈을 호출하여 사용해야 한다.
# [깊은 복사]
# ex: import copy
#     Lst1 = [1, 2, 3]
#     Lst2 = copy.deepcopy(Lst1)

#[예제 3] : List 복사
ls =[10,20,30,40]
arr = ls    #얇은 복사
arr[2] = 20000
print("ls:{}\tls id:{}".format(ls,id(ls)))    #id 함수는 주소를 확인하는 함수
print("arr:{}\tls id:{}".format(arr,id(arr)))   #arr은 ls의 얇은 복사이기때문에 arr을 작업해도 ls를 작업한것과 같다. 주소값 역시 같다.

import copy
ls =[10,20,30,40]
arr = copy.deepcopy(ls)    #깊은 복사
arr[2] = 20000
print("ls:{}\tls id:{}".format(ls,id(ls)))  #arr2값인 30이 그대로 출력
print("arr:{}\tls id:{}".format(arr,id(arr)))   #arr2값인 30을 200000으로 바꿔 출력. id값 역시 ls와 다른것을 확인할수 있다.

# [List 함수 사용]
# List는 단순한 데이터 저장 용도로만 사용하지 않고, 다양한 부가적인 함수를 같이 사용한다.

# Append 함수 사용 : 데이터 추가
lst = [1, 2, 3]
print(lst)
lst.append(4)   #appen는 list끝에다가 추가할 때 사용한다.
print(lst)
lst.append([5,'a']) #list속에 list를 넣는 2차원 list사용 가능
print(lst)

# Extend 함수 사용 : 데이터 다수 추가
lst = [1,2,3]
lst.extend(['a','b','c'])   #extend는 확장개념. list에 여러개를 추가시킬 때 사용한다.
print(lst)

# Insert 함수 사용 : 데이터 삽입
lst = [1,2,3]
lst.insert(1,'b')   #1번 인덱스에 b값을 삽입
print(lst)
# Pop 함수 사용(Insert에 이어서.) : 데이터 삭제
lst.pop(1)  #1번 인덱스 값 삭제(b값)
print(lst)
lst.pop()   #번호 지정을 안하면 리스트 마지막 값 삭제
print(lst)

# Remove 함수 사용 : 데이터 삭제
lst = [1,'b','c']
lst.remove('c')
print(lst)

# Claer 함수 사용 : 리스트 초기화
lst = [1,2,3,4,5,6,7,8,9,0]
lst.clear()
print(lst)

# Count 함수 사용 : 지정한 값의 갯수 반환
lst = [1,2,3,4,5,6,1]
print(lst.count(1)) #1값이 2개 있다.

# Index 함수 사용 : 지정한 값에 인덱스 번호값 반환
lst = [1,2,3]
print(lst.index(2)) #값 2가 들어있는 인덱스 번호는?

# Reverse 함수 사용 : 리스트 값의 역순
lst = [1,2,3,4,5,6,7,8,9]
lst.reverse()
print(lst)

# Sort 함수 사용 : 리스트 정렬
lst = [12,56,123,96,234]
lst.sort(reverse=False) #오름차순
print(lst)
lst.sort(reverse=True)  #내림차순
print(lst)

# [문제 1] : 리스트 초기 값 [30, 20, 10] 설정 후 아래와 같이 출력 되도록 코드를 작성하세요.
# 현재 리스트 : [30, 20, 10]
# append(40) 후의 리스트 : [30, 20, 10, 40]
# pop() 으로 추출한 값 : 40
# pop() 후의 리스트 : [30, 20, 10]
# sort() 후의 리스트 : [10, 20, 30]
# reverse() 후의 리스트 : [30, 20, 10]

lst = [30, 20, 10]
lst.append(40)
print("append(40) 후의 리스트 :",lst)
print("pop()으로 추출한 값 : {}".format(lst.pop()))
print("pop() 후의 리스트 :",lst)
lst.sort(reverse=False)
print("sort() 후의 리스트 :",lst)
lst.reverse
print("reverse() 후의 리스트 :",lst)

# [문제 2] : 리스트 초기 값 [30, 20 ,10] 설정 후 아래와 같이 출력 되도록 코드를 작성하세요.
# 현재 리스트 : [30, 20, 10]
# 10 값의 위치 : 2
# insert(2, 200) 후의 리스트 : [30, 20, 200, 10]
# remove(200) 후의 리스트 : [30, 20, 10]
# extend ([555, 666, 555]) 후의 리스트 : [30, 20, 10, 555, 666, 555]
# 555 값의 개수 : 2

lst = [30, 20, 10]
print("현재 리스트 :",lst)
print("10 값의 위치 :",lst.index(10))
lst.insert(2, 200)
print("insert(2, 200) 후의 리스트 :",lst)
lst.remove(200)
print("remove(200) 후의 리스트 :",lst)
lst.extend([555, 666, 555])
print("extend([555, 666, 555] 후의 리스트 :",lst)
print("555 값의 개수 :",lst.count(555))

# 2차원 리스트(리스트 속에 리스트, 상위 리스트와 하위 리스트 존재)
# arr[0][2] - 0번째 리스트 속 2번째 첨자

aa = [[1,2,3,4,],   # 이렇게 정렬해 놓으면 보기 쉽고 이해하기 좋음
      [5,6,7,8,],   # 첨자를 찾기에 편리
      [9,10,11,12]]
print(aa[1])    #1번째 하위리스트 [5,6,7,8] 출력
print("[0][0]",aa[0][0])    #1
print("[0][1]",aa[0][1])    #2
print("[0][2]",aa[0][2])    #3
print("[0][3]",aa[0][3])    #4
print("[1][0]",aa[1][0])    #5
print("[1][1]",aa[1][1])    #6

aa = [[1,2,3,4,],   # 이차원 리스트 이중  For문으로 표현하기
      [5,6,7,8,],
      [9,10,11,12]]
for i in range(3):  #3은 라인 수(1,5,9)
    for j in range(4):  #4는 칸의 수(1,2,3,4 ...)
        print(aa[i][j],end='\t')
    print()
'''
ls_1 = []; ls_2 = []; value = 1 #list에 값이 아직 정해지지 않음 정의
for i in range(0,3):
    for k in range(0,4):
        ls_1.append(value)
        value += 1
    ls_2.append(ls_1)
    ls_1 = []   #ls_1 초기화
for i in range(3):
    for j in range(4):
        print(ls_2[i][j], end='\t')
    print()
print(ls_2)


