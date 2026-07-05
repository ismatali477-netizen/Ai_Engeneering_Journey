def contains_duplicate(l):
    s=set()
    for item in l:
        if item not in s:
            s.add(item)
        else:
            return True
    else:
        return False
print(contains_duplicate([1, 2, 3, 1]))
