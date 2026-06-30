from collections import Counter
def sales_count(l):
    return dict(Counter(l))
print(sales_count(["apple","banana","apple"]))
