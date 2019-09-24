# [Dictionary]
# : List와 유사하다, List와 같이 첨자를 이용하여 특정 요소에 접근
# : 첨자를 Key 값으로 사용한다. (즉, Key가 값을 가르키고 있다.)
# : 탐색속도가 빠르며, 사용하기 편리하다.
# : Dictionary 정의 시 "{}"를 이용한다.
# : 데이터 정의는 Key:Value 형식을 사용한다.
'''
#[예제.1]
student = {"학번":1234,"이름":"홍길동","학과":"IT학과"}
print(type(student))
print(student)
print(student["학번"])
print(student["이름"])
print(student["학과"])

#예제.2
impo = {}
impo["파이썬"] = "www.python.org"
impo["네이버"] = "www.naver.com"
impo["구글"] = "www.google.com"
print(impo)

#예제.3
impo = {}
name = input("키 입력:")
val = input("값 입력:")
impo[name] = val
print(impo)

[ Dictionary 문제 ]
Key값과 Value값을 입력 받아 저장 후 출력 하시오.
이름(key) 입력 : 겐지
값(value) 입력 : 수리검
이름(key) 입력 : 맥크리
값(value) 입력 : 섬광탄
이름(key) 입력 : 파라
값(value) 입력 : 로켓런처
이름(key) 입력 : 리퍼
값(value) 입력 : 샷건
이름(key) 입력 : 솔저
값(value) 입력 : 나선로켓
* 출력 예시 *
{'솔저': '나선로켓', '맥크리': '섬광탄', '리퍼': '샷건', '파라': '로켓런처', '겐지': '수리검'}

over = {}
for i in range(5):
    k = input("이름(Key) 입력:")
    v = input("값(Value) 입력:")
    over[k] = v
print(over)

#예제.4
dic = {1:'a',2:'b',3:'c'}
dic.update({4:'d'})
print(dic.get(1))
print(dic.get(4))
print(dic.get(9))

#예제.5
k = ['a','b','c','d']
dic1 = {}.fromkeys(k)
dic2 = {}.fromkeys(k,1)
print(dic1)
print(dic2)

#예제.6
dic = {1:"일",2:"이",3:"삼",4:"사"}
print("dic keys = {}".format(dic.keys()))
print("dic values = {}".format(dic.values()))
print("list = {}".format(list(dic)))
print("list keys = {}".format(list(dic.keys())))
print("list Values = {}".format(list(dic.values())))

#예제.7
singer = {}
singer["이름"] = input("가수 이름:")
singer["구성원"] = input("인원수:")
singer["대표곡"] = input("대표곡:")
print()
for i in singer.keys():
    print("{}:{}".format(i,singer[i]))

#예제.8
dic = {1:'a',2:'b',3:'c',4:'d'}
print(dic)
dic.pop(2)
print(dic)
dic.clear()
print(dic)

# 메뉴등록 프로그램 만들기
import os
menu = {}
num = 0
wh = True
while wh:
    print("==========================")
    print("1.메뉴 등록")
    print("2.메뉴 별 가격")
    print("3.메뉴 가격 수정")
    print("4.종료")
    print("==========================")
    num = int(input("번호 입력:"))

    if num == 1:
        name = input("메뉴이름:")
        if menu.get(name) == None:
            menu[name] = input("가격:")
        else:
            print("입력하신 메뉴는 이미 존재 합니다.")

    elif num == 2:
        for key,value in menu.items():
            print(key,"\t",value)
        os.system("pause")

    elif num == 3:
        name = input("수정 할 메뉴 이름:")
        if menu.get(name) == None:
            print("입력하신 메뉴는 존재하지 않습니다.")
        else:
            menu[name] = input("가격:")

    elif num == 4:
        wh = False
        print("프로그램 종료")

    else:
        print("번호를 다시 입력하세요.")
    os.system("cls")

[ Quiz 1 ] : 네비게이션 주소 등록 프로그램 만들기. [ Navi.exe 실행 파일 ]
1.주소 등록
2.주소 수정
3.주소 목록
4.검색
5.종료
'''
import os
navi = {}
num = 0
wh = True
while wh:
    print()
    print("======================================================")
    print("1.주소등록  2.주소수정  3.주소목록  4.검색  5.종료")
    print("======================================================")
    num = int(input("번호입력:"))
    if num == 1:
        name = input("목적지 이름:")
        if navi.get(name) == None:
            navi[name] = input("목적지 주소:")
            print("등록완료")
            os.system("pause")
        else:
            print("입력하신 목적지는 이미 존재합니다.")
            os.system("pause")

    elif num == 2:
        name = input("수정하실 목적지 이름:")
        if navi.get(name) == None:
            print("입력하신 목적지 존재하지 않습니다.")
            print("정확히 다시 입력해 주세요.")
            os.system("pause")
        else:
            navi[name] = input("목적지 주소:")
            print("수정완료")
            os.system("pause")

    elif num == 3:
        for key,val in navi.items():
            print(key,"\t",val)
        os.system("pause")

    elif num == 4:
        name = input("검색하실 목적지 이름:")
        if navi.get(name) == None:
            print("입력하신 목적지는 존재하지 않습니다.")
        else:
            print(navi.get(name))
            os.system("pause")

    elif num == 5:
        wh = False
        print("프로그램 종료")
        os.system("pause")
    else:
        print("번호를 다시 입력하세요.")
    os.system("cls")


