'''
str = "string indexing"
print(str[0])
print(str[2])
print(str[4])
print(str[7])
print(str[8])
print(str[-1])
print(str)

str = "string indexing"
for i in str: 
    print(i,end="")

str = "Have a"
print(str)
str += " nice day"
print(str)
print(str * 3)
print("0" * 10)

str = "Python is Easy. Programming 할만하네요"
print("str: ",str)
print()
print("str.upper(): ",str.upper())
print("str.lower(): ",str.lower())
print("str.title(): ",str.title())

[Quiz.1]
"NevEr-eVer 100glVe Up" [ 변경 전 ]
"Never-Ever 100Glve Up" [ 변경 후 ]

str = "NevEr-eVer 100glVe Up"
print(str.title())

st = "Have a nice day"
print("st:",st)
print()
print("st변수안에 'a'문자의 갯수 : ",st.count('a'))
print("st변수안에 'day'문자열의 갯수 : ",st.count('day'))
print("st변수안에 'dak'문자열의 갯수 : ",st.count('dak'))

#아래의 코드를 String Count 함수를 이용하여 간편화 하세요.
st = "It is a fun python class"
cnt_a=cnt_s=cnt=0
for i in st:
    cnt+=1
    if i == 'a':
        cnt_a+=1
    elif i == 's':
        cnt_s+=1
print("문자열의 길이:{}".format(cnt))
print("문자 'a'의 개수:{}".format(cnt_a))
print("문자 's'의 개수:{}".format(cnt_s))

st = "It is a fun python class"
print("문자열의 길이:{}".format(len(st)))
print("문자 'a'의 개수:{}".format(st.count('a')))
print("문자 's'의 개수:{}".format(st.count('s')))

st = "Have a nice day"
print("st : ", st)
print("day의 위치(find): ",st.find("day"))
print("day의 위치(index): ",st.index("day"))
print("kkk의 위치(find): ",st.find("kkk"))
print("kkk의 위치(index): ",st.index("kkk"))

print(st.find('a'))
print(st.find('a',2))
print(st.find('a',6))
print(st.find('a',14))

[ Quiz ] : List를 정의 하여 첨자 위치 저장
           a의 총 개수와 첨자의 위치를 출력 하시오
st = 'Have a nice day Have a nice day Have a nice day‘
[결과]
a 개수 : 9
첨자 : [1, 5, 13, 17, 21, 29, 33, 37, 45]

st = "Have a nice day Have a nice day Have a nice day"
cnt = 0
ls = []
for i in st:
    cnt = st.find('a',cnt)
    if cnt != -1:
        ls.append(cnt)
        cnt += 1
print("a의 갯수 : ", st.count('a'))
print("첨자: ",ls)

st = " 파 이 썬 " # 공백기준
print("st\t\t:{}{}{}".format("*",st,"*"))
print("st.strip()\t:{}{}{}".format("*",st.strip(),"*"))

st = "파이썬파" # "파" 기준
print("st :",st)
print("st.strip():", st.strip("파"))

st = "---파---이---썬---"
print("st.strip():",st.strip("-"))
print("st.strip():",st.rstrip("-"))
print("st.strip():",st.lstrip("-"))

st = "2019/02/01"
print("st : ",st)
print("replace() : ",st.replace('/',':'))
print("replace() : ",st.replace(st[0:4],"2020"))

st = """
오늘 하루도 즐겁게
오늘 하루도 행복하게
오늘 하루도 최선을
"""
print(st)

[ Quiz ] : replace의 활용 , ":" 첨자를 구하여 Slicing 활용
st = """김개똥 -2017년 03월 24일
홍길동구리 -2015년 04월 02일
선우선녀 -2018년 05월14일
"""
위의 내용을 아래와 같이 변경 하시오 
"– (바)" ▶ ":(콜론으로 변경)", 년도를 1999년으로 모두 변경 

[결과]
김개똥 :1999년 03월 24일
홍길동구리 :1999년 04월 02일
선우선녀 :1999년 05월14일

st = """김개똥 -2017년 03월 24일
홍길동구리 -2015년 04월 02일
선우선녀 -2018년 05월14일
"""
st = st.replace("-",":")
i = 0
for k in range(st.count(":")):
    i = st.find(":",i+1)
    print("i",i)
    st=st.replace(st[i+1:i+5],"1999")
print(st)

st = """
Never ever give up
Never ever give up
Never ever give up
"""
print(st)
print(st.split())
print(st.splitlines())

st = "하나:둘:셋"
print(st.split(":"))
st = "일,이,삼"
print(st.split(","))
print(st.split())

li = ["","123","456"]
print("공백join:","".join(li))

'''






