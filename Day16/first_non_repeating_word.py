from collections import Counter
def first_non_repeating_word(s):
    d=dict(Counter(s.split()))
    for item in s.split():
        if d[item]==1:
            return item
    else:
        return None
print(first_non_repeating_word(
    "ai ai python python "
))
