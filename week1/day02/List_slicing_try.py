def flip(lst):
    return lst[ : : -1]

def get_evenIndexMember(lst):
    return lst[0 : (len(lst) + 1) : 2]

print(get_evenIndexMember([0,1,2,3,4,5,6,7,8,9,10]))
print(flip([0,1,2,3,4,5,6,7,8,9,10]))