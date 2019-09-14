'''
# [문제 6]
# 1 ~ 100 사이의 값 중 3의 배수이며, 5의 배수에 해당하는 합을 구하시오.
sum = 0
for i in range(1, 100, 1):
    if i % 3 == 0:
        if i % 5 == 0:
            sum += i
print(sum)

# [문제 7]
# 두 수를 입력 받아 입력 받은 두 수의 범위 안의 합을 구하시오.
su1 = int(input("작은 수를 입력하시오:"))
su2 = int(input("큰 수를 입력하시오:"))
sum1 = 0
for i in range(su1, su2+1, 1):  #증가값이 1인경우 생략가능
    if i >= su1 and i <= su2:
        sum1 += i
print("{}와 {}사이의 합:{}".format(su1,su2,sum1))

# [문제 8]
# Turtle을 이용한 다각형 그리기(반복문 사용)
import turtle
angle = int(input("각을 입력(3~n):"))
for i in range(1, angle):
    turtle.forward(100)
    turtle.left(360 / angle)
turtle.forward(100)
turtle.mainloop()

# [이중(중첩) For문]
#for x in range(반복횟수) :     x가 10이면 반복코드 10번
#     for y in range(반복횟수) :    y가 10이면 반복코드 100번 -> 상위 for문의 값은 하위 for문의 값이 모두 진행 된 다음에 진행
#        수행 코드 
#    수행 코드 
#수행 코드

# [예제 1]
for x in range(1, 4):
    print("첫 번쨰 for문 시작!")
    for y in range(1, 3):
        print("두 번째 for문 시작!")

# [예제 2] : 이중 for문 이해하기 좋은 예제
for i in range(0,3,1):
    for k in range(0,5,1):
        print("이중 for문 (i:{}\tk:{})".format(i,k))

# [문제 1]
# 중첩 for문을 이용하여 구구단을 가로 출력하시오.
for i in range(2, 10, 1):
    for k in range(1, 10, 1):
        print("{} X {} = {}\t".format(i,k,i*k),end="")
        if k % 9 == 0:
            print()

# [문제 2]
# 중첩 for문을 이용하여 구구단을 세로 출력하시오.
for i in range(1, 10, 1):
    for k in range(2, 10, 1):
        print("{} X {} = {}\t".format(k,i,i*k),end="")
        if k % 9 == 0:
            print()

# [문제 3]
#상위포문0 일때하위포문:0 0 0 0 0
#상위포문1 일때하위포문:0 1 2 3 4
#상위포문2 일때하위포문:0 2 4 6 8
#상위포문3 일때하위포문:0 3 6 9 12
#상위포문4 일때하위포문:0 4 8 12 16
for i in range(0,5,1):
    print("상위포문{} 일때하위포문:".format(i),end='')
    for j in range(0,5,1):
        print(i*j,'', end='')
    print()

# [문제 4] : 이중 for문을 이용하여 아래와 같이 출력하시오.
#1   2   3   4   5
#6   7   8   9   10
#11  12  13  14  15
#16  17  18  19  20
#21  22  23  24  25

for i in range(0,5):
    for j in range(1,6):
        print(j+5*i, end="\t")
    print()

# while반복문 : 무한 반복 시킬 때 사용 多
# [예제 1]
i = 1
odd, even = 0, 0
while i<= 10:
    if i % 2 == 0:
        even += i
    else:
        odd += i
    i += 1
print("1~10 짝수의 합:", even)
print("1~10 홀수의 합:", odd)

# [예제 2]
# 잘못 된 무한반복
while True:
    print("망함") #Ctrl + c

# [예제 3]
# 무한 루프 활용
i = 1
flag = True
while flag:
    print("{}.종속문장".format(i), end='')
    if i == 10:
        flag = False    #break 사용으로 루프문 빠져나가기
    i += 1
'''














