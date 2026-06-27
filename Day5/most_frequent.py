def most_frequent(l):
    count=0
    repeated=0
    for i in l:
        curr=l.count(i)
        if (curr>repeated):
            repeated=curr
            count=i
    return count       
print(most_frequent([10,10,10,20]))
