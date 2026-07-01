def sort_names(l):
    return [item['name'] for item in sorted(l,key=lambda x:x['name'])]

print(sort_names([
    {"name":"John"},
    {"name":"Ali"},
    {"name":"Sara"}
]))
