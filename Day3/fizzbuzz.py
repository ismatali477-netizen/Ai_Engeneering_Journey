def fizzbuzz(n):
    l=[]
    for num in range(1,n+1):
        if num%3==0 and num%5==0:
            l.append("fizzbuzz")
        elif num%3==0:
            l.append("fizz")
        elif num%5==0:
            l.append("buzz")
        else:
            l.append(num)
    return l

print(fizzbuzz(15))
