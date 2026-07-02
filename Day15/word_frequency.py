from collections import Counter
def word_frequency(s):
    return dict(Counter(s.split()))
print(word_frequency("ai is fun ai"))
