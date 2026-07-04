from collections import Counter
def most_common_word(s):
    l=dict(Counter(s.split()))
    return max(l,key=l.get)
print(most_common_word(
    "ai python ai data ai data data"
))
