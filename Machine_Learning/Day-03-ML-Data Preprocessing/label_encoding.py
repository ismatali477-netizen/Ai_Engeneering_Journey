from sklearn.preprocessing import LabelEncoder
def encode_labels(labels):
    leb=LabelEncoder()
    return leb.fit_transform(labels)
if __name__=="__main__":
    animals = [
        "cat",
        "dog",
        "dog",
        "bird",
        "cat"
    ]
    print(encode_labels(animals))