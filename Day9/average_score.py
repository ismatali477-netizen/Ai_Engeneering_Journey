def average_score(d):
    return (sum(d.values()))/len(d) if len(d)>0 else 0
print(average_score({}))
