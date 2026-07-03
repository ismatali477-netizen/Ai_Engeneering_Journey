def sort_words_by_length(s):
    return sorted(s.split(),key=len)
print(sort_words_by_length(
    "python ai is awesome"
))
