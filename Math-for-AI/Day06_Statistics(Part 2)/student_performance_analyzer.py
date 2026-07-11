import numpy as np
def student_report(student):
    return(float(np.mean(student)),float(np.median(student)),float(np.var(student)),float(np.std(student)),int(np.max(student)-np.min(student))
        )
def normalize_subjects(matrix):
    return  np.round((matrix - np.min(matrix,axis=0)) / (np.max(matrix,axis=0) - np.min(matrix,axis=0)),2)

def best_consistency(matrix):
    return np.argmin(np.std(matrix,axis=1))+1

students = np.array([
    [90, 85, 80],
    [78, 88, 91],
    [65, 70, 75],
    [95, 92, 89]
])
if __name__=="__main__":
    for i,student in enumerate(students,start=1):
        mean,median,var,std,range=student_report(student)
        print(f"Student {i} Report:\n Mean: {mean:.2f}\nMedian: {median:.2f}\nVar: {var:.2f}\nStandard Deviation: {std:.2f}\nRange: {range:.2f}")
    print(f"Normalized Student: \n{normalize_subjects(students)}")
    print(f"Most Consistent Student:\nStudent {best_consistency(students)}")