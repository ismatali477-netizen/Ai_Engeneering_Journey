def best_department(l):
    d={}
    count={}
    for item in l:
        marks=item['marks']
        salary=item['salary']
        dept=item['dept']
        if dept not in d:
            d[dept]=marks+salary
            count[dept]=1
        else:
            d[dept]+=marks+salary
            count[dept]+=1
    total_average= {dept: d[dept] / count[dept] for dept in d}
    return max(total_average,key=total_average.get)
print(best_department([
    {"dept":"AI","salary":5000,"marks":80},
    {"dept":"AI","salary":3000,"marks":60},
    {"dept":"Web","salary":4500,"marks":90}
]))
