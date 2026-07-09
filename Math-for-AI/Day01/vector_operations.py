def add_vectors(v1, v2):
    return [a + b for a, b in zip(v1, v2)]

def subtract_vectors(v1, v2):
    return [a - b for a, b in zip(v1, v2)]

def scalar_multiply(vector, scalar):
    return [item*scalar for item in vector]

v1 = [2, 4]
v2 = [1, 3]

print(add_vectors(v1, v2))
# [3, 7]

print(subtract_vectors(v1, v2))
# [1, 1]

print(scalar_multiply(v1, 3))
# [6, 12]