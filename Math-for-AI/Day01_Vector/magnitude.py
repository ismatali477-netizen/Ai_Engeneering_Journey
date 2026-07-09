import math
def magnitude(vector):
    add=sum(item*item for item in vector)
    return math.sqrt(add)
if __name__ == "__main__":
    print(magnitude([3,4]))