from sklearn.model_selection import train_test_split
def split_dataset(features, labels):
    return train_test_split(features,labels,test_size=0.25,random_state=42)
if __name__=="__main__":
    hours = [[1],[2],[3],[4],[5],[6],[7],[8]]
    scores = [35,45,55,65,75,85,92,96]
    X_train, X_test, y_train, y_test = split_dataset(hours, scores)

    print("Training Features:", X_train)
    print("Testing Features :", X_test)
    print("Training Labels  :", y_train)
    print("Testing Labels   :", y_test)