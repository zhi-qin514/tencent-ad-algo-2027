L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1  if isinstance(x, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('pass!')
else:
    print('failed!')
