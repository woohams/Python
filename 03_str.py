# 문자 (single  quotation, double quotation 차이없음)
# \ : escape sequence

# single * 1
a = 'a/nb\'s'
print(a)

# single * 3
b = '''a
b\tc
d'''
print(b)

# double * 1
c="abc\"s"
print(c)

# double * 3
d = """a
b\tc
d"""
print(d)

# 혼합
e = 'abc"def"\'ghi'
print(e)
f = "abc'def'\"ghi"
print(f)

# 문자열 계산
str01 = "Hello, "
str02 = "World!"
print(str01 + str02)
print(str01*3 + str02)

