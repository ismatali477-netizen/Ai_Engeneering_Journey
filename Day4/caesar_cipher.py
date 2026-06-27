def caesar_cipher(s):
    n=""
    for i in s:
        if i=="z":
            n+="a"
            continue
        alpha=chr(ord(i)+1)
        n+=alpha
    return n
print(caesar_cipher("abzc"))
