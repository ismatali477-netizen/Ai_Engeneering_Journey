def separate_features_labels(data):
    return [item[0] for item in data],[item[1] for item in data]
students = [
    [2, 45],
    [4, 60],
    [6, 75],
    [8, 90]
]

if __name__=="__main__":
    features,labels=separate_features_labels(students)
    print(f"Features={features}\nLabels={labels}")