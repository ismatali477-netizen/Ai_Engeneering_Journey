def highest_salary_department(l):
    d={}
    for item in l:
        dept=item["dept"]
        salary=item["salary"]
        if dept not in d:
            d[dept]=salary
        else:
            d[dept]+=salary
    return max(d,key=d.get)
print(highest_salary_department([
    {"dept":"AI","salary":5000},
    {"dept":"Web","salary":4000},
    {"dept":"AI","salary":3000}
]))
