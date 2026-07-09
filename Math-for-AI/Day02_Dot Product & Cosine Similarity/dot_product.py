def dot_product(v1, v2):
    if len(v1)!=len(v2):
        raise ValueError("Both students must have the same number of subjects.")
    return sum((a*b) for a,b in zip(v1,v2))
v1 = [2, 3]
v2 = [4, 5]
print(dot_product(v1, v2))