def highest_subject(l):
    seen=set()
    d={}
    for item in l:
        marks=item['marks']
        subject=item['subject']
        if subject not in seen:
            d[subject]=marks
            seen.add(subject)
        else:
            d[subject]+=marks
    return max(d,key=d.get)

print(highest_subject([
    {"subject":"Math","marks":35},
    {"subject":"Science","marks":70},
    {"subject":"Math","marks":30}
]))
