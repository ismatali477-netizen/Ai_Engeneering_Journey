from collections import Counter
def most_common_char(s):
    d=dict(Counter(s))
    max_value=max(d.values())
    for item in d:
        if max_value==d[item]:
            return item
print(most_common_char("mississippi"))
