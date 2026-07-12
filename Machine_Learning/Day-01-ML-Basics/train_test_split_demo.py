from sklearn.model_selection import train_test_split
features = [2, 4, 6, 8]
labels = [45, 60, 75, 90]
test_size = 0.25
random_state = 42
def split_dataset(features, labels):
    return train_test_split(features,labels,test_size=test_size,random_state=random_state)

if __name__=="__main__":
    X_train,X_test,y_train,y_test=split_dataset(features,labels)
    print("X_train:", X_train)
    print("X_test :", X_test)
    print("y_train:", y_train)
    print("y_test :", y_test)