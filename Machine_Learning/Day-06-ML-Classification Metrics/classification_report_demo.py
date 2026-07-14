from sklearn.metrics import classification_report
def create_report(actual, predicted):
    return classification_report(actual,predicted)
if __name__ == "__main__":
    actual = [1,1,1,0,0,1]
    predicted = [1,1,0,0,0,1]

    print(create_report(actual, predicted))