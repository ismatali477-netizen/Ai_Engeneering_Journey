import math
def magnitude(vector):
    add=sum(item*item for item in vector)
    return math.sqrt(add)
print(magnitude([3,4]))