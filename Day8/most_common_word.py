from collections import Counter
def most_common_word(s):
    d=dict(Counter(s.split()))
    repeated=0
    word=""
    for item in d:
        if d[item]>repeated:
            repeated=d[item]
            word=item
    return word

print(most_common_word("ai ai python ai"))
