from collections import Counter
def count_words(s):
    s1=s.split()
    return dict(Counter(s1))
print(count_words("ai is fun ai"))
