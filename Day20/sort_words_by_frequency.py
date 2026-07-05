from collections import Counter
def sort_words_by_frequency(s):
    d=dict(Counter(s.split()))
    return sorted(d,key=d.get,reverse=True)
print(sort_words_by_frequency(
    "ai python ai data ai data"
))
