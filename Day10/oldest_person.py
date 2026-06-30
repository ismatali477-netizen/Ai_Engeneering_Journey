def oldest_person(l):
    oldest=max(l,key=lambda x:x['age'])
    return oldest['name']
print(oldest_person([
    {"name":"Ali","age":20},
    {"name":"Sara","age":25},
    {"name":"John","age":22}
]))
