# list

a = list()
print(a)
a.append(1)
print(a)
a[0] = 'a'
print(a)
a.append('b')
print(a)

# []를 사용해서 생성
b = [1,2,3,4,5]
print(b)

# 0번지 + 3번지 결과값 출력
print(b[0] + b[3])

# reverse
b.reverse()
print(b)

# sort
b.sort()
print(b)

# 중첩
c = ['a','b','c','d','e',['f','g','h','i']]
print(c)
print(c[5])
print(c[5][2])

# list + list
print(b+c)
