def word_length_frequency(s):
    d={}
    l=s.split()
    for item in l:
        length=len(item)
        if length not in d:
            d[length]=1
        else:
            d[length]+=1
    return d
print(word_length_frequency(
    "ai is fun python"
))
