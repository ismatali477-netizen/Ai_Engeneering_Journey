def highest_paid(l):
    highest= max(l,key=lambda x:x['salary'])
    return highest['name']
print(highest_paid([
    {"name":"Ali","salary":5000},
    {"name":"Sara","salary":7000},
    {"name":"John","salary":6000}
]))
