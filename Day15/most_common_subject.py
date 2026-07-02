def most_common_subject(l):
    d={}
    for item in l:
        subject=item['subject']
        if subject not in d:
            d[subject]=1
        else:
            d[subject]+=1
    return max(d,key=d.get)

print(most_common_subject([
    {"subject":"Math"},
    {"subject":"Science"},
    {"subject":"Math"}
]))
