def most_frequent_employee(l):
    d={}
    for item in l:
        name=item['name']
        if name not in d:
            d[name]=1
        else:
            d[name]+=1
    return max(d,key=d.get)

print(most_frequent_employee([
    {"name":"Ali"},
    {"name":"Sara"},
    {"name":"Ali"}
]))
