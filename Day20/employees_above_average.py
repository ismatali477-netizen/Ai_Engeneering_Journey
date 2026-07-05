def employees_above_average(l):
    d={}
    for item in l:
        salary=item['salary']
        name=item['name']
        d[name]=salary
    return [item for item in d if d[item]>sum(d.values())/len(l)]

print(employees_above_average([
    {"name":"Ali","salary":5000},
    {"name":"Sara","salary":7000},
    {"name":"John","salary":4000}
]))
