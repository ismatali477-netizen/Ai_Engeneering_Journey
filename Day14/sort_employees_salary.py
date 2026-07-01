def sort_employees_salary(l):
    return list(reversed([x['name'] for x in sorted(l,key=lambda x:x['salary'])]))

print(sort_employees_salary([
    {"name":"Ali","salary":5000},
    {"name":"Sara","salary":7000},
    {"name":"John","salary":4000}
]))
