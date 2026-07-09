import math
def dot_product(v1, v2):
    if len(v1)!=len(v2):
        raise ValueError("Both vector must have same length!!")
    return sum((a*b) for a,b in zip(v1,v2))
def magnitude(vector):
    add=sum(item*item for item in vector)
    return math.sqrt(add)
def cosine_similarity(v1, v2):
    return dot_product(v1,v2)/(magnitude(v1)*magnitude(v2))

if __name__ == "__main__":
    v1 = [1,2]
    v2 = [2,4]
    print(cosine_similarity(v1, v2))