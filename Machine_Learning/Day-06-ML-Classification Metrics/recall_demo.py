from sklearn.metrics import recall_score
def calculate_recall(actual, predicted):
    return recall_score(actual,predicted)
actual =    [1,1,1,0,0,1]
predicted = [1,1,0,0,0,1]
if __name__=="__main__":
    print(f"Recall: {calculate_recall(actual, predicted):.2f}")