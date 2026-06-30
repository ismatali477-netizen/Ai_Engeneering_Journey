def above_average(d):
    average=(sum(d.values()))/len(d) if len(d)>0 else 0
    return [item for item in d if d[item]>average]

print(above_average({"Ali": 80, "Sara": 90, "John": 70}))
