def filter_students(l):
    return [x['name'] for x in l if x["marks"]>=80]
print(filter_students([
    {"name":"Ali","marks":80},
    {"name":"Sara","marks":95},
    {"name":"John","marks":70}
]))
