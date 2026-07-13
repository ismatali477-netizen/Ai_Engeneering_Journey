from sklearn.preprocessing import StandardScaler,LabelEncoder
import numpy as np
def scale_hours(hours):
    scale=StandardScaler()
    return np.round(scale.fit_transform(hours),2)

def encode_study_type(types):
    leb=LabelEncoder()
    return leb.fit_transform(types)
if __name__ == "__main__":
    hours = np.array([[1],[2],[3],[4],[5],[6],[7],[8]])

    study_type = ["online","offline","online","offline","online","offline","online","offline"]
    print("Scaled Hours:")
    print(scale_hours(hours))

    print("\nEncoded Study Type:")
    print(encode_study_type(study_type))