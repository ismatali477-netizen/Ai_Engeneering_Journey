from sklearn.metrics import r2_score
def calculate_r2(actual, predicted):
    return r2_score(actual,predicted)
if __name__=="__main__":
    actual = [50, 60, 70, 80]
    predicted = [52, 58, 69, 81]
    print(f"R² Score: {calculate_r2(actual, predicted):.3f}")