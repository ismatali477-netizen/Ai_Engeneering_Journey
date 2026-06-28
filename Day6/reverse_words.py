def reverse_words(s):
    s1=s.split()
    s1.reverse()
    return " ".join(s1)

print(reverse_words("AI is awesome"))
