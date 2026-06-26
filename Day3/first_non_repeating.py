def first_not_repeating_character(s):
    for l in s:
        if s.count(l)==1:
            return l
print(first_not_repeating_character("abc"))
