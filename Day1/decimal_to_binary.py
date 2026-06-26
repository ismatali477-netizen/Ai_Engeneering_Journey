def binary(n):
    if n==0:
        return 0
    list=[]
    while n>0:
        result=n%2
        list.append(str(result))
        n=n//2
    list.reverse()
    return "".join(list)
print(binary(8))
