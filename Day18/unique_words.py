def unique_words(s):
    seen=set()
    l=[]
    for item in s.split():
        if item not in seen:
            seen.add(item)
            l.append(item)
    return l
print(unique_words("ai ai is fun fun"))
