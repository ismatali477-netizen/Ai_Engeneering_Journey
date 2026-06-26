def largest(list):
    largest=list[0]
    for num in list:
        if num>largest:
            largest=num
    return largest
print(largest([4,6,9,2,14,7]))
