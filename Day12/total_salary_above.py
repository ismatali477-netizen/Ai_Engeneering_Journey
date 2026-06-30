def total_salary_above(l,m):
    return sum(x['salary'] for x in l if x['salary']>m)

print(total_salary_above(
[
    {"name":"Ali","salary":5000},
    {"name":"Sara","salary":7000},
    {"name":"John","salary":4000}
], 4500))
