'''
# [Python 파일 입출력]
# - 디스크상에 존재하는 파일을 읽어들일 수 있다.
# - 디스크에 파일을 생성하여, 저장 할 수 있다.
# - 많은 양의 데이터를 처리 할 때 주로 사용
# - Ex: 홈페이지의 이미지 데이터, 게임 이미지, 음악 파일, 많은 양의 텍스트

# [File Access 과정]
# 1. open 함수를 이용하여 파일을 open 상태로 변경
# 2. "read or write" 등의 함수를 이용하여 파일에 대한 작업 처리를 진행
# 3. "close" 함수를 이용하여 파일을 닫아준다.

# File Open 방법
# : "변수" = open("open file(경로명)", "파일 접근 형태")
# :    [종류]          [지정 한 File이 존재하는 경우]                   [지정 한 File이 존재하지 않는 경우]
# :  "r(read)"           File을 읽기 전용으로 Open                 실제 File이 존재해야 읽기 전용으로 Open이 가능
# :  "w(write)"    기존의 내용을 삭제 후 쓰기 전용으로 Open            새로운 File을 생성, 쓰기 전용으로 Open
# :  "a(append)"     기존의 내용 끝에 쓰기 전용으로 Open               새로운 File을 생성, 쓰기 전용으로 Open


# [작업 경로] :
# D:\\1월 평일반 Python기초 진우현\\Python_Test

# [예제 1]
file = open("D:\\1월 평일반 Python기초 진우현\\Python_Test\\.test.txt","a",encoding="utf-8") #경로의 test.txt파일을 w형태로 오픈하겠다.
                                                                            #visual studio 인코딩 형식이 utf-8, 이렇게 설정해줘야 txt파일이 안깨짐
str1 = input("문서의 내용을 입력:")
file.write(str1)
file.close

# [문제]
# 1. 본인의 인적 사항을 파일에 저장 후 출력하세요. (이름, 나이, 주소)
# - 당신의 이름은 : 홍길동
# - 홍길동 님의 나이는 : 20살
# - 홍길동 님의 주소는 : 산골짜기
# - 저장한 파일의 내용을 다른 파일에 그대로 저장도 진행
# - 라인은 변경되어야 합니다.
file = open("D:\\1월 평일반 Python기초 진우현\\Python_Test\\.test1.txt","a",encoding="utf-8")
str1 = input("당신의 이름은 : ")
str2 = input("{} 님의 나이는 : ".format(str1))
str3 = input("{} 님의 주소는 : ".format(str1))
file.write(str1+'\n'+str2+'\n'+str3)
file.close

file = open("D:\\1월 평일반 Python기초 진우현\\Python_Test\\.test1.txt","r",encoding="utf-8")
test1 = file.read()
file.close()
print(test1)

file2 = open("D:\\1월 평일반 Python기초 진우현\\Python_Test\\.test2.txt","w",encoding="utf-8")
file2.write(test1)  # 복사 개념
file2.close()

# [예제 2]
file = open("D:\\1월 평일반 Python기초 진우현\\Python_Test\\.test1.txt","r",encoding="utf-8")
line1 = file.readline()
line2 = file.readline()
line3 = file.readline()
line4 = file.readline()
print(line1)
print(line2)
print(line3)
print(line4)
if line4 == '':
    print("더 이상 값이 존재하지 않습니다.")
    file.close()

# [반복문으로 변경]
file = open("D:\\1월 평일반 Python기초 진우현\\Python_Test\\.test1.txt","r",encoding="utf-8")
while True:
    readline1 = file.readline()
    if readline1 == "":
        print("값 없음")
        file.close()
        break
    print(readline1)

# [readlines] 사용]
file = open("D:\\1월 평일반 Python기초 진우현\\Python_Test\\.test1.txt","r",encoding="utf-8")
buf = file.readlines()
for st in buf:
    print(st, end='')
file.close()

# [문제]
# 1. info.txt 파일에 저장 되어있는 값을 불러온 후 수정 값을 입력하여 값을 수정 후 다시 파일로 저장
#    readlines 함수를 사용
file = open("D:\\1월 평일반 Python기초 진우현\\Python_Test\\.test1.txt","r",encoding="utf-8")
buf = file.readlines()
i = 0
for st in buf:
    print(i,":",end='')
    i+=1
file.close()

file = open("D:\\1월 평일반 Python기초 진우현\\Python_Test\\.test1.txt","w",encoding="utf-8")
i = int(input("\n수정 할 번호 입력:"))
temp = input("수정 할 값 입력:")
buf[i] = temp + "\n"    #buf 라는 리스트 i번 첨자에 temp + \n 을 넣어라
for indata in buf:
    file.write(indata)
file.close()

# [예제 3]
# - ord() 함수 : 문자의 고유한 숫자 값을 표시
# - chr() 함수 : 숫자의 해당하는 문자 값을 표시
print(ord('안'))
print(ord('녕'))
print(ord('1'))
print(ord('2'))
print(ord('a'))

print(chr(50504))
print(chr(45397))
print(chr(49))
print(chr(50))
print(chr(97))
'''
# 암호화
readStr, outStr = '',''
secu = 100
choice = input("1.파일 저장\t2.파일 불러오기: ")
filename = input("파일명 입력:")
if choice == "1":
    content = input("파일의 내용을 입력하세요(단일문자!):")
    outFile = open(filename,'w',encoding='utf-8')
    chNum = ord(content)
    chNum = chNum + secu
    content = chr(chNum)
    outFile.write(content)
    outFile.close()
# 복호화
elif choice == "2":
    readFile = open(filename,'r',encoding='utf-8')
    readStr = readFile.read()
    chNum = ord(readStr)
    chNum = chNum - secu
    readStr = chr(chNum)
    print("파일에서 가져 온 값:", readStr)
    readFile.close()


