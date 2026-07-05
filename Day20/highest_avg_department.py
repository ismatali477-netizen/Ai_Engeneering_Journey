def highest_avg_department(l):
    d={}
    count={}
    for item in l:
        salary=item['salary']
        dept=item['dept']
        if dept not in d:
            d[dept]=salary
            count[dept]=1
        else:
            d[dept]+=salary
            count[dept]+=1
    d1={item:(d[item]/count[item]) for item in d}
    return max(d1,key=d1.get)
print(highest_avg_department([
    {"dept":"AI","salary":5000},
    {"dept":"AI","salary":3000},
    {"dept":"Web","salary":4500}
]))
