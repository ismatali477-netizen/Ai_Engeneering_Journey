from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
def train_model(X_train, y_train):
    model=LinearRegression()
    model.fit(X_train,y_train)
    return model

def evaluate(model, X_test, y_test):
    return r2_score(y_test,model.predict(X_test))
if __name__=="__main__":
    hours = [[1],[2],[3],[4],[5],[6],[7],[8]]
    scores = [35,45,55,65,75,85,92,96]
    X_train, X_test, y_train, y_test = train_test_split(
        hours,
        scores,
        test_size=0.25,
        random_state=42
    )
    model = train_model(X_train, y_train)
    print(f"Test R² Score: {evaluate(model, X_test, y_test):.3f}")