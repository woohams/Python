'''
# [예제 1]
while True:
    print("무한반복 테스트")
    break
    print("2번째 출력")
print("반복 종료")

# [예제 2]
while True:
    i = int(input("10보다 작은 정수 입력:"))
    if i < 10:
        print("10보다 작은 정수입력")
        break
    else:
        print("다시 입력하세요.")
        continue    #조건식 True로 이동 : 다시 입력하세요. 출력
        print("테스트") #실행되지 않음
print("반복 종료!")

# [문제 1]
# 쌀 100통이 저장되어 있는 창고에 암수 1쌍의 쥐가 있다.
# 쥐 한마리가 하루에 20g씩의 쌀을 먹고, 10일(10, 20,30)마다 쥐의 수가 2배씩 증가한다.
# 며칠만에 창고의 쌀이 모두 쥐의 먹이가 될까. 그리고 쥐는 총 몇마리 인가?
# (쌀 한통 = 1kg) (쌀을 먹은 후 2배 증가하는 조건)
rice = 100000; mouse = 2; day = 1;  #쌀을 kg -> g으로 변경, 초기 쥐의 마리 수, 날짜
while rice > 0:
    rice -= mouse * 20; #rice = rice - mouse * 20
    if day % 10 == 0:   #10의 배수일때 마다 쥐의 마리수 증가
        mouse *= 2
    if rice <= 0:
        break;
    day += 1
print("{}일, {}마리".format(day, mouse))

# [문제 2]
# 별찍기, 홀수를 입력 받아 입력 받은 홀수 라인만큼 마름모 형태의 별이 나타나도록 하세요.
# [EX] : 홀수의 줄 수 입력 : 5
#  ★
# ★★★
#★★★★★
# ★★★
#  ★
# [힌트]
# Flag(기준점 설정하기), 공백은 감소 후 증가, 별은 증가 후 감소
# If문, For문을 활용
# 공백의 시작은 전체 라인에서 나누기 2한 몫이 시작 값,
# 별은 초기 값이 항상 1로 시작 된다.
i, j, num = 0, 0, 1;
while num:  #무한 반복
    ln = int(input("홀수의 줄 수를 입력: "))
    flag = 0; sp = ln // 2; st = 1  # sp = 공백, st = 별
    for i in range(ln):
        #출력 부분
        for j in range(sp):     # 공백 출력
            print(" ", end='')
        for j in range(st):     # 별 출력
            print("★", end='')
        print()

        if i == (ln//2):    #flag 기법
            flag = 1
        if flag == 0:
            sp -= 1; st += 2
        else:
            sp += 1; st -= 2
    num = int(input("계속:(1) / 종료:(0)"))
print("프로그램 종료")
'''
#[문제 3]
price = int(input("요금을 투입하세요:"))
i, j, num = 0, 0, 1;
coffee = 200; cocoa = 250;
print("==========커피자판기==========")
print("1.커피(200) 2.코코아(250) 3.잔돈 반환 4.종료") 
while num:
    flag = 0;
    for i in range(price):
        print()
            
        if i == 1:
            flag =1
            price -= coffee
        if i == 2:
            flag=1
            price -= cocoa
        if i == 3:
            flag=1
            print("잔액:{}".format(price))
        if i == 4:
            flag=0
            print("종료")
            break;





























































