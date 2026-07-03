def lowest_student(l):
    top_student= min(l,key=lambda x:x['marks'])
    return top_student['name']

print(lowest_student([
    {"name":"Ali","marks":80},
    {"name":"Sara","marks":60},
    {"name":"John","marks":70}
]))
