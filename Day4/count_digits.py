def count_integer(s):
    count=0
    for i in s:
        if i.isdigit():
            count+=1
    return count
print(count_integer("abc123"))
