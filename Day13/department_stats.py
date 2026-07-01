def department_stats(l):
    d={}
    for item in l:
        dept=item['dept']
        salary=item['salary']
        if dept not in d:
            d[dept]={"employees":1,"salary":salary}
        else:
            d[dept]["employees"]+=1
            d[dept]["salary"]+=salary
    return d
print(department_stats([
    {"dept":"AI","salary":5000},
    {"dept":"AI","salary":3000},
    {"dept":"Web","salary":4000}
]))
