# 09_built_in.py

# int() : 정수
print(int(True))
print(int(False))
print(int(43.78))
print(int('80'))

# 2진수
print(int('11111', 2))

# 8진수
print(int('77', 8))

# 16진수
print(int('FF', 16))

# float() : 실수
print(float(3))
print(float('3'))

# complex() : 복소수
print(7j)
print(type(7j))
print(1+7.56j)

a = 1+7.56j
print(a.real)
print(a.imag)

# str() : 문자열
b = 100
print('b = ' + str(b))
print(str('Hello, World!'))
print(repr('Hello, World!'))
