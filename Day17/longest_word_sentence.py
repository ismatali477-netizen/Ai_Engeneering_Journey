def longest_word_sentence(s):
    longest=0
    word=""
    for item in s.split():
        if len(item)>longest:
            longest=len(item)
            word=item
    return word
print(longest_word_sentence(
    "AI engineering is awesome"
))
