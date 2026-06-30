def average_salary(l):
    d={}
    count={}
    for item in l:
        dept=item["dept"]
        salary=item["salary"]
        if dept not in d:
            d[dept]=salary
            count[dept]=1
        else:
            d[dept]+=salary
            count[dept]+=1
    return {item:d[item]/count[item] for item in d}
print(average_salary([
    {"dept":"AI","salary":5000},
    {"dept":"AI","salary":3000},
    {"dept":"Web","salary":4000}
]))
