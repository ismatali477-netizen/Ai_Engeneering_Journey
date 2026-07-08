def valid_parentheses(s):
    stack=[]
    d={")":"(","}":"{","]":"["}
    for item in s:
        if item in d:
            top_element=stack.pop() if stack else '#'
            if d[item]!=top_element:
                return False
        else:
            stack.append(item)
    return len(stack)==0
        

print(valid_parentheses("([{}])"))