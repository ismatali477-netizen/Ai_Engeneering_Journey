def count_passed_students(l):
    return sum(1 for item in l if item['marks']>=40)
print(count_passed_students([
    {"name":"Ali","marks":80},
    {"name":"Sara","marks":30},
    {"name":"John","marks":50}
]))
