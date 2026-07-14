from sklearn.metrics import precision_score
def calculate_precision(actual, predicted):
    return precision_score(actual,predicted)
actual = [1,1,1,0,0,1]
predicted = [1,1,0,0,0,1]
if __name__=="__main__":
    print(f"Precision: {calculate_precision(actual, predicted):.2f}")