def highest_scoring_student(l):
    top_student= max(l,key=lambda x:x['marks'])
    return top_student['name']

print(highest_scoring_student([
    {"name":"Ali","marks":80},
    {"name":"Sara","marks":95},
    {"name":"John","marks":70}
]))
