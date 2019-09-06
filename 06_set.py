#set(집합) 중복x, 순서x

# [list] 생성자로 
a = set(['1', '2', '3', '3',])
print(a)
print(type(a))

# 생성자에 iterable한 객체를 넣으면 set의 값으로 변환
b = set('hello')
print(b)

# {}를 사용해서
c = {'a', 'b', 'c', 'hello', '1', '2', '3'}
print(c)

c.add('world')
print(c)

# 합집합
print(a.union(b))
print(a|b)

# 교집합
print(a.intersection(c))
print(a&c)


