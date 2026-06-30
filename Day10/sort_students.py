def sort_students(l):
    l1=sorted(l,key=lambda x:x['marks'])
    l2=[item['name'] for item in l1]
    l2.reverse()
    return l2
print(sort_students([
    {"name":"Tom","marks":50}
]))
