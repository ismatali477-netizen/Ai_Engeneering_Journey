import numpy as np
def average_student(students):
    return np.round(np.mean(students, axis=1),2)
def average_subject(students):
    return np.round(np.mean(students, axis=0),2)
def highest_student(students):
    return np.argmax(np.mean(students,axis=1))+1
def highest_subject(students):
    return np.argmax(np.mean(students,axis=0))+1
students = np.array([
    [90, 85, 80],
    [78, 88, 91],
    [65, 70, 75]
])
if __name__=="__main__":
    print(f"Average of student:{average_student(students)}")
    print(f"Average of Subject:{average_subject(students)}")
    print(f"Highest Scoring Student:{highest_student(students)}")
    print(f"Highest Average Subject:{highest_subject(students)}")