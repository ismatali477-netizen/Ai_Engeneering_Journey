def smallest_L(n):
    smallest=n[0]
    for num in n:
        if num<smallest:
            smallest=num
    return smallest
print(smallest_L([4,2,7,9,1]))
