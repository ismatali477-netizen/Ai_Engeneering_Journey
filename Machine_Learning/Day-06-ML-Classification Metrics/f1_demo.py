from sklearn.metrics import f1_score
def calculate_f1(actual, predicted):
    return f1_score(actual,predicted)
if __name__ == "__main__":
    actual = [1,1,1,0,0,1]
    predicted = [1,1,0,0,0,1]

    print(f"F1 Score: {calculate_f1(actual, predicted):.2f}")