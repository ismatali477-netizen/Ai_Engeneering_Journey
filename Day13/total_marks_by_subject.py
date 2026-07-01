def total_marks_by_subject(l):
    d={}
    for item in l:
        sub=item['subject']
        mark=item['marks']
        if sub not in d:
            d[sub]=mark
        else:
            d[sub]+=mark
    return d


print(total_marks_by_subject([
    {"subject":"Math","marks":80},
    {"subject":"Science","marks":70},
    {"subject":"Math","marks":20}
]))
