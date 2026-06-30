def count_department(l,m):
    return sum(1 for x in l if x["dept"].lower()==m.lower())
print(count_department(
[
    {"name":"Ali","dept":"AI"},
    {"name":"Sara","dept":"Web"},
    {"name":"John","dept":"AI"}
], "web")
)
