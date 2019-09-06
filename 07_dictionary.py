# dictionary    key : value

# 생서자를 통해서 만들어 보자!
dict01 = dict()
dict01[1] = 'one'
dict01[2] = 'two'
print(dict01)

# {}를 통해서 만들어 보자!
dict02 = {}
dict02['one'] = 1
dict02['two'] = 2
dict02['3'] = 3
print(dict02)

# key/value 가져오기
print(dict01.get(1))
print(dict02.get('one'))

print(dict01.keys())
print(dict02.values())

print(list(dict01.keys()))
print(type(dict01.keys()))

print(list(dict02.values())[1])
