from sklearn.metrics import confusion_matrix 
def create_confusion_matrix(actual, predicted):
    return confusion_matrix(actual,predicted)
if __name__=="__main__":
    actual = [1, 0, 1, 1, 0]
    predicted = [1, 0, 1, 0, 0]
    print(create_confusion_matrix(actual, predicted))