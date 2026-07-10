import numpy as np
def student_statistics(student):
    return (float(np.mean(student)),float(np.median(student)),int(max(student)-np.min(student)))
def class_statistics(matrix):
    return np.mean(matrix,axis=0)
def best_subject(matrix):
    return np.argmax(np.mean(matrix,axis=0))+1
students = np.array([
    [90, 85, 80],
    [78, 88, 91],
    [65, 70, 75],
    [95, 92, 89]
])
if __name__=="__main__":
    for i,student in enumerate(students,start=1):
        print(f"Report of student {i} = {student_statistics(student)}")
    print(f"Mean of subject: {class_statistics(students)}")
    print(f"Best subject: {best_subject(students)}")
    