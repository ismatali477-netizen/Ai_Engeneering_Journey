def longest_word(l):
    word=""
    longest=0
    for item in l:
        if len(item)>longest:
            longest=len(item)
            word=item
    return word
print(longest_word(["AI","Engineer"]))
