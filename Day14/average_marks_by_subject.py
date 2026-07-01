def average_marks_by_subject(l):
    d={}
    count={}
    for item in l:
        marks=item['marks']
        subject=item['subject']
        if subject not in d:
            d[subject]=marks
            count[subject]=1
        else:
            d[subject]+=marks
            count[subject]+=1
    return {subject: d[subject] / count[subject] for subject in d}
print(average_marks_by_subject([
    {"subject":"Math","marks":80},
    {"subject":"Math","marks":60},
    {"subject":"Science","marks":90}
]))
