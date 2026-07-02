def char_position(s):
    d={}
    for i,item in enumerate(s):
        if item not in d:
            d[item]=[i]
        else:
            d[item].append(i)
    return d
print(char_position("hello"))
