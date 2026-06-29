def top_scorer(d):
    highest=0
    name=""
    for item in d:
        if d[item]>highest:
            highest=d[item]
            name=item
    return name
print(top_scorer({"Ali": 98, "Sara": 95, "John": 90}))
