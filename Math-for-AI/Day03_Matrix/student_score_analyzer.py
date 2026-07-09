def average_student(student):
    return sum(student)/len(student)
def average_subject(matrix):
    return [sum(subject)/len(matrix) for subject in zip(*matrix)]
def highest_student(matrix):
    result= [sum(item) for item in matrix]
    return result.index(max(result))+1
def highest_subject_average(matrix):
    sub=[sum(subject)/len(matrix) for subject in zip(*matrix)]
    return f"Subject {sub.index(max(sub))+1}"
students = [
    [90, 85, 80],
    [78, 88, 91],
    [65, 70, 75]
]
if __name__=="__main__":
    for i in range(len(students)):
        print(f"Average of student {i} is {round(average_student(students[i]),2)}")#85
    print(f"Average of each Subject:{average_subject(students)}")
    print(f"Highest Scoring Student:{highest_student(students)}")
    print(f"Highest Average Subject:{highest_subject_average(students)}")
