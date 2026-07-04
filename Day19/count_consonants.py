def count_consonants(s):
    return sum(1 for item in "".join(s.split()) if item not in "aeiou")
print(count_consonants("hello world"))
