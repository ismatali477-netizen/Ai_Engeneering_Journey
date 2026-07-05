def department_summary(l):
    d={}
    for item in l:
        salary=item['salary']
        dept=item['dept']
        if dept not in d:
            d[dept]={}
            d[dept]["employee"]=1
            d[dept]["total_salary"]=salary
            d[dept]["average_salary"]=salary/d[dept]["employee"]
        else:
            d[dept]["employee"]+=1
            d[dept]["total_salary"]+=salary
            d[dept]["average_salary"]=d[dept]["total_salary"]/d[dept]["employee"]
    return d
print(department_summary([
    {"dept":"AI","salary":5000},
    {"dept":"AI","salary":3000},
    {"dept":"Web","salary":4000}
]))
