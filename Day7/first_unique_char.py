def first_unique_char(s):
    result=0
    for item in s:
        if s.count(item)==1:
            result=item
            break
    else:
        return None
    return result
print(first_unique_char("aabbc"))
