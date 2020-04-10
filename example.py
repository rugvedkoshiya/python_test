def how(l):
    flag = 0
    for i in l:
        if type(i) == list:
            flag += 1
    return flag

lists = [1,2,[2,3,4],[5,4,7,[1,[2,32]]]]
print(how(lists))

