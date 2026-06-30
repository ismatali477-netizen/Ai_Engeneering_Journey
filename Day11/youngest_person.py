def youngest_person(l):
    youngest=min(l,key=lambda x:x['age'])
    return youngest['name']
print(youngest_person([
    {"name":"Ali","age":20},
    {"name":"Sara","age":25},
    {"name":"John","age":18}
]))
