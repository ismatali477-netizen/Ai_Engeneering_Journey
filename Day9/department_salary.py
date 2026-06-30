def department_salary(l):
    d={}
    for item in l:
        salary=item["salary"]
        dept=item["dept"]
        if dept not in d:
            d[dept]=salary
        else:
            d[dept]+=salary
    return d
print(department_salary([
    {"name":"Ali","dept":"AI","salary":5000},
    {"name":"Sara","dept":"Web","salary":4000},
    {"name":"John","dept":"AI","salary":3000}
]))
