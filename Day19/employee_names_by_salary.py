def employee_names_by_salary(l):
    return [x['name'] for x in sorted(l,key=lambda x:x['salary'])]

print(employee_names_by_salary([
    {"name":"Ali","salary":5000},
    {"name":"Sara","salary":3000},
    {"name":"John","salary":4000}
]))
