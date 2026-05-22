def trim(s):
    head = 0
    end = len(s) - 1

    # 当and表达式第一个表达式为false则右边不执行避免了空list【0】out of range
    while head <= end and s[head] == ' ':
        head += 1
    while end >= head and s[end] == ' ':
        end -= 1
    return s[head:end + 1]

# 测试:
if trim('hello  ') != 'hello':
    print('no1!')
elif trim('  hello') != 'hello':
    print('no2!')
elif trim('  hello  ') != 'hello':
    print('no3!')
elif trim('  hello  world  ') != 'hello  world':
    print('no4!')
elif trim('') != '':
    print('no5!')
elif trim('    ') != '':
    print('no6!')
else:
    print('Yes!')
