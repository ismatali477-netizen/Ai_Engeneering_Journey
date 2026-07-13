from sklearn.metrics import accuracy_score
def calculate_accuracy(actual, predicted):
    return accuracy_score(actual,predicted)
if __name__=="__main__":
    actual = [1, 0, 1, 1, 0]
    predicted = [1, 0, 1, 0, 0]
    print(f"Accuracy: {calculate_accuracy(actual, predicted):.2f}")