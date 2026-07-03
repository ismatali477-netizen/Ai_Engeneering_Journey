def count_vowels(s):
    return sum(1 for item in s if item in "aeiou")
print(count_vowels("hello world"))
