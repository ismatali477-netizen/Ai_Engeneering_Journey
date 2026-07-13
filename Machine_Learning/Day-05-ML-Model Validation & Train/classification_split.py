from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
def split_data(features, labels):
    return train_test_split(features,labels,test_size=0.25,random_state=42)
def train_classifier(X_train, y_train):
    model=LogisticRegression()
    model.fit(X_train,y_train)
    return model

def test_classifier(model, X_test, y_test):
    return accuracy_score(y_test,model.predict(X_test))
if __name__=="__main__":
    hours = [[1],[2],[3],[4],[5],[6],[7],[8]]
    result = [0,0,0,0,1,1,1,1]
    X_train, X_test, y_train, y_test = split_data(hours, result)
    model = train_classifier(X_train, y_train)
    accuracy = test_classifier(model, X_test, y_test)
    print(f"Test Accuracy: {accuracy:.2f}")