def valid_parentheses(s):
    count=0
    for i in s:
        if "(" in i:
            count+=1
        elif ")" in i:
            count-=1
        if count<0:
            return False
    return count==0

print(valid_parentheses("())()"))
