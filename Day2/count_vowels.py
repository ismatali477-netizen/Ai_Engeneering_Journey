def count_vowel(s):
    count=0
    for i in range(len(s)):
        if(s[i].lower() in "aeiou"):
            count += 1
    return count
print(count_vowel("Ismat"))
