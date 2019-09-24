'''
# [문제 1] : 날짜 및 시간 별 일정 등록 프로그램 작성 // 힌트 : 날짜 - 키에 등록, 할 일 - 리스트에 등록

import copy
info = {}; data = []; data2 = []; wh=True; num=0
while wh:
    print("==================================================")
    print("1.일정표 등록    2.검색  3.종료")
    print("==================================================")
    num = int(input("번호 입력:"))
    if num == 1:
        data.append(input("날짜 입력:"))
        print("시간 별 일정 등록")
        time = int(input("몇 개의 일정을 등록 하시겠습니까?"))
        for i in range(time):
            data2.append(input("일정등록 형식(시간:할 일)"))
        info[data[0]] = copy.deepcopy(data2)    #데이터2를 딥카피해서 info의 데이터 0번첨자에 대입
    elif num ==2:
        day = input("일정을 확인 할 날짜입력:")
        if info.get(day) == None:
            print("해당 날짜는 일정이 존재하지 않습니다.")
        else:
            print("{}의 일정은 {}입니다.".format(day, info.get(day)))
    elif num == 3:
        print("프로그램 종료")
        wh = False
        data.clear()
        data2.clear() #list 초기화
'''
# [문제 2] : 학생의 인적사항 등록 후 검색하는 프로그램을 만드시오 [중복 확인 x]
# [ Info.exe 실행 파일]
# (학번, 이름, 주소 ,등급(A,B,C,D,E,F), (dic = '학번{dic}))
# 1. 학생 등록
# 2. 학생 검색
# 3. 학생 수정
# 4. 학생 삭제
# 5. 전체 학생 목록
# 6. 종료

import copy
import collections #데이터가 여러개 있을 때 목록화 할수 있게 해줌
info = {}; wh=True; num=0; number=0; gr=''; addr=''; name='';
info2 = collections.OrderedDict()  #info2를 OrdereDict 으로 지정한다.(info2를 목록화 시킴)
while wh:
    print("=====================================")
    print("1.학생 등록\n2.학생 검색\n3.학생 수정\n4.학생 삭제\n5.전체 학생 목록\n6.종료")
    print("=====================================")
    num = int(input("번호 입력:"))
    if num ==1:
        number = int(input("학번 입력:"))
        name = input("학생 이름:")
        addr = input("학생 주소:")
        gr = input("학생 등급:")
        info2["학번"] = number; info2["이름"] = name; info2["주소"] = addr; info2["등급"] = gr; #info2를 dic로 사용, key값에 각각 매칭시켜줌
        info[number] = copy.deepcopy(info2) #info2를 딥카피 시켜 info-number키 값에 가져온다. 학번이 키값이 되는것, list를 써서 append 해도 상관x
        info2.clear()   #초기화 시켜주는게 좋음
        print("등록 완료!")
    elif num == 2:
        number = int(input("학번 입력:"))
        if info.get(number) == None:
            print("입력 하신 학번은 존재하지 않습니다.")
        else:
            print("학번 {}의 정보는 {} 입니다.".format(number, info.get[number]))
    elif num == 3:
        number = int(input("학번 입력:"))
        if info.get(number) == None:
            print("입력 하신 학번은 존재하지 않습니다.")
        else:
            print("학번 {}의 정보는 {} 입니다.".format(number, info.get[number]))
            val = input("수정 항목 입력:")
            change = input("변경 정보 입력:")
            info[number][val] = change  #number는 info의 키, val은 키 값에 매치된 dic의 값  
                                        #2차원 리스트 개념이랑 동일하다. dic안에 dic이라 key값을 두번 지정
            print("수정 완료")
    elif num == 4:
        number = int(input("학번 입력:"))
        if info.get(number) == None:
            print("입력 하신 학번은 존재하지 않습니다.")
        else:
            print("학번 {}의 정보는 {} 입니다.".format(number, info.get[number]))
            info.pop(number)
            print("삭제 완료")
    elif num == 5:
        for k, v in info.items():
            print(k,"\t",v)
    elif num == 6:
        print("프로그램 종료")
        wh = False
    else:
        print("잘못 입력하셨습니다.")            

