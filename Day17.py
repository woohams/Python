
'''
#문제.1
def calc(num1,num2=1,op='+'):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
print(calc(2,1,'-'))  # 결과 값 : 1 
print(calc(2,1))      # 결과 값 : 3 (op = '+')
print(calc(3))        # 결과 값 : 4 (num2 = 1)
print(calc(3,op='-')) # 결과 값 : 2 (num2 = 1)

# 문제.2
def vSum(*numbers):
    sum = 0
    for x in numbers:
        sum += x
    return sum
print(vSum(1,2))
print(vSum(1,2,3))
print(vSum(1,2,3,4,5))
print(vSum(1,2,3,4,5,6,7,8,9,10))

#[예제.1] : Reverse Code 작성 ( 123 -> 321 )
def reversecode(num1):
    temp = 0
    while True:
        temp = int(num1%10)
        num1 = int(num1/10)
        print(temp,end="")
        if not num1: # 기억!
            break;

print("Reverse Code!")
num1 = int(input("수 입력:"))
reversecode(num1)

# 예제.2 : 함수 내부에서 또 다른 함수 호출
def func2(a,b):
    a+=5; b*=5
    print("func2 a:{}, b:{}".format(a,b))

def func1():
    a=5; b=10
    func2(a,b)
    print("func1 a:{}, b:{}".format(a,b))
func1()

# 예제.3
def sum_func(*par): # Tuple 형식으로 인자값을 저장
    result = 0
    print(type(par))
    print(par)
    for x in par:
        result += x
        print(x)
    return result
sum = 0
sum = sum_func(10,20)
print(sum)
sum = sum_func(10,20,30,40,50)
print(sum)

# 예제.4
def change(a,b,c):
    return a+10,b+20,c+30 # Tuple 형식의 반환

a,b,c=change(10,20,30)
print(a,b,c)

d = change(10,20,30)
print(d,type(d))

# 예제.5
def dic_func(**par):
    print(type(par))
    print(par)
    for k in par.keys():
        print("{}:{}마리!".format(k,par[k]))
dic_func(피카츄=3,꼬부기=1,파이리=0)

[Quiz]
1. 짝, 홀수를 구분하는 함수를 작성해 주세요.
2. "3"의 배수를 판별하는 함수를 작성해 주세요.
3. 계산기를 입력,출력,연산기능으로 나눠서 실행되게 작성해 주세요.
4. 거꾸로 수를 반환하는 함수를 계산,출력 기능으로 나눠서 작성해 주세요.
5. 자판기를 선택,출력 기능으로 나눠서 함수화 하여 작성해 주세요.
'''



































