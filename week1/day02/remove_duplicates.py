# 保留顺序去重
def remove_duplicates(lst):
    d1 = {}
    result = []
    for x in lst:
        if x not in d1:
            d1[x] = True
            result.append(x)
    return result