def highest_salary_by_department(l):
    d={}
    for item in l:
        dept=item['dept']
        salary=item['salary']
        if dept not in d:
            d[dept]=salary
        else:
            if salary>d[dept]:
                d[dept]=salary
    return d


print(highest_salary_by_department([
    {"dept":"AI","salary":5000},
    {"dept":"AI","salary":7000},
    {"dept":"Web","salary":4000}
]))
