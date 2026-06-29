
def remove_duplicate_words(s):
    d=[]
    s1=s.split()
    for item in s1:
        if item not in d:
            d.append(item)
    return " ".join(d)
print(remove_duplicate_words("ai ai is fun"))
