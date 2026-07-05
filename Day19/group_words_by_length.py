def group_words_by_length(s):
    d={}
    l=s.split()
    for item in l:
        length=len(item)
        if length not in d:
            d[length]=[item]
        else:
            d[length].append(item)
    return d
print(group_words_by_length(
    "ai is fun python"
))
