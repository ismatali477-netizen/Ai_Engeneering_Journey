import math
def add_bonus(student, bonus):
    return [item+bonus for item in student]

def total_marks(student):
    return sum(item for item in student)

def distance(student1, student2):
    if len(student1) != len(student2):
        raise ValueError("Both students must have the same number of subjects.")
    squared_sum=sum((a-b)**2 for a, b in zip(student1,student2))
    return round(math.sqrt(squared_sum),2)
ali = [90, 85, 80]
sara = [92, 81, 79]
john = [65, 70, 60]
print(add_bonus(ali, 5))
# [95, 90, 85]
print(total_marks(ali))
# 255
print(distance(ali, sara))
#4.58