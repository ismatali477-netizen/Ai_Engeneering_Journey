def longest_name(l):
    longest= max(l,key=lambda x:len(x['name']))
    return longest['name']
print(longest_name([
    {"name":"Ali"},
    {"name":"Alexander"},
    {"name":"Sara"}
]))
