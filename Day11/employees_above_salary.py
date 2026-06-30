def employees_above_salary(l,m):
    d={}
    for item in l:
        salary=item['salary']
        name=item['name']
        if name not in d:
            d[name]=salary
    return [item for item in d if d[item]>m]
    """ALTERNATIVELY
    def employees_above_salary(l, m):
    return [x["name"] for x in l if x["salary"] > m]
    """

print(employees_above_salary(
[
    {"name":"Ali","salary":5000},
    {"name":"Sara","salary":7000},
    {"name":"John","salary":4000}
], 5000))
