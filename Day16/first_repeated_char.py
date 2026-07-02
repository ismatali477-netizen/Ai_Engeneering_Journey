def first_repeated_char(s):
    d={}
    for item in s:
        if item not in d:
            d[item]=1
        else:
            return item
    else:
        return None
print(first_repeated_char("abcd"))
