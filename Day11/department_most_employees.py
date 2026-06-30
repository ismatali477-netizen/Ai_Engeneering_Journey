def department_most_employees(l):
    d={}
    for item in l:
        dept=item["dept"]
        if dept not in d:
            d[dept]=1
        else:
            d[dept]+=1
    return max(d,key=d.get)
print(department_most_employees([
    {"name":"Ali","dept":"AI"},
    {"name":"Sara","dept":"Web"},
    {"name":"John","dept":"AI"}
]))
