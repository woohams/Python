'''
# [for 문]
# : 주어진 반복 횟수에 따라 반복적으로 코드를 실행 할 때 사용한다.
# : 변수를 정의하고, 범위를 설정하여 반복 횟수를 결정한다.
# : EX (0(초기값), 10(종료값),1(증감값))

# [예제 1]
for i in range(0, 10, 1):   #i에 0값이 들어가 10까지 1씩 증가한다.
    print("For문 Test [i = {}]".format(i))
print("For문 종료")

# [문제]
# : 1 ~ 10까지의 합을 구하시오 (for문 사용)
sum = 0
for i in range(0, 11, 1):
    sum += i # sum = sum + i
print(sum)

# [문제 1]
i, sum = 0, 0
start, end, grow = 0, 0, 0
start = int(input("시작 값 입력:"))
end = int(input("종료 값 입력:"))
grow = int(input("증가 값 입력:"))
for i in range(start, end+1, grow):
    sum += i
print(sum)

# [예제 2]
for val in "string":
    print(val)

# []
print("출력테스트", end="test") #Python에서는 print끝에 end함수 \n이 포함되어 있다.
print("출력테스트2")

#[예제 3]
for x in range(1, 10, 1):
    print(x, end="안녕")

# [문제 2]
# For문과 If문을 이용하여 아래와 같이 출력
#1   2   3   4   5
#6   7   8   9   10
#11  12  13  14  15
#16  17  18  19  20
#21  22  23  24  25
#26  27  28  29  30
for x in range(1, 31, 1):
    print(x,"\t", end="")
    if x % 5 == 0:
        print("")

# [문제 3]
# 변수 st = "It is a fun Python class" 다음 문자열 중에서
# 알파벳 'a'의 개수와 's'의 개수를 구하시오.
st = "It is a fun Python class"
a = s = 0
for i in st:
    if i == 'a':
        a += 1
    elif i == 's':
        s += 1
print("a의 개수:{}, s의 개수:{}".format(a,s))

# [문제 4]
# 수를 입력 받아 1 ~ 입력받은 수 까지 짝수의 합과 홀수의 합을 구해 출력
su = int(input("수를 입력:"))
evensum, oddsum = 0, 0
for i in range(1, su+1, 1):
    if i % 2 == 0:
        evensum += 1
    else:
        oddsum += 1
print("짝수 합:", evensum)
print("홀수 합:", oddsum)

# [문제 5]
# 시작 값, 끝 값, 증가값(1)을 입력받아 시작과 끝 값 사이의 7의 배수만 출력
i, su = 0 ,0
start = int(input("시작 값 입력:"))
end = int(input("끝 값 입력:"))
grow = int(input("증가 값 입력:"))
for su in range(start, end+1, grow):
    if su % 7 == 0:
        print(su)
print("이상 {}와 {}값 사이의 7의 배수".format(start, end))
'''



























