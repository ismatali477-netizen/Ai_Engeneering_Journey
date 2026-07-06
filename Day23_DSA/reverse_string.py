def reverse_string(s):
    l=list(s)
    left=0
    right=len(s)-1
    while left<right:
        l[left],l[right]=l[right],l[left]
        left+=1
        right-=1
    return "".join(l)
print(reverse_string("hello"))
