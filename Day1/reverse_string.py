def rev(s):
    lst=[]
    for i in range(len(s)):
        lst.append(s[i])
    lst.reverse()
    return "".join(lst)
print(rev("name"))
