from collections import Counter
def top_k_frequent(l,k):
    d=Counter(l)
    return sorted(d,key=d.get,reverse=True)[:k]
print(top_k_frequent([5,5,5,1,1,2,2,2,3], 3))
