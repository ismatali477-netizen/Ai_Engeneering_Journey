def anagram_check(s,n):
    return sorted(s.lower())==sorted(n.lower())
print(anagram_check("listen", "silent"))
