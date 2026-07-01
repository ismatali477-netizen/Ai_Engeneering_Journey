def top_department(l):
    d={}
    count={}
    for item in l:
        marks=item['marks']
        dept=item['dept']
        if dept not in d:
            d[dept]=marks
            count[dept]=1
        else:
            d[dept]+=marks
            count[dept]+=1
    averages = {dept: d[dept] / count[dept] for dept in d}
    return max(averages, key=averages.get)

print(top_department([
    {"dept":"AI","marks":80},
    {"dept":"AI","marks":60},
    {"dept":"Web","marks":90}
]))
