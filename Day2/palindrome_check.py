def is_palindrome(s):
    s1="".join(reversed(s))
    if s.lower()==s1.lower():
        return "Palindrome"
    else:
        return "Not Palindrome"

print(is_palindrome("Madam"))

