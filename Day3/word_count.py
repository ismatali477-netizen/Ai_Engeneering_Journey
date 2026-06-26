def word_count(s):
    d={}
    l=s.split()
    for word in l:
        d[word]=l.count(word)
    return d
print(word_count("name name ismat"))
