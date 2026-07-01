def passed_students(l):
    return [x['name'] for x in l if x['marks']>=40]
print(passed_students([
    {"name":"Ali","marks":80},
    {"name":"Sara","marks":30},
    {"name":"John","marks":50}
]))
