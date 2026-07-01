def department_names(l):
    d={}
    for item in l:
        dept=item["dept"]
        name=item["name"]
        if dept not in d:
            d[dept]=[]
        d[dept].append(name)
    return d
print(department_names([
    {"name":"Ali","dept":"AI"},
    {"name":"Sara","dept":"Web"},
    {"name":"John","dept":"AI"}
]))
