from collections import Counter
def majority_element(l):
    d=Counter(l)
    return max(d,key=d.get)
print(majority_element([2,2,1,1,1,2,2]))
