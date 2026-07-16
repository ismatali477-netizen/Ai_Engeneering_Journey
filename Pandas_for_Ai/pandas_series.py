import pandas as pd
import numpy as np
marks = [90, 85, 95, 88, 76]
marks_series=pd.Series(marks)
print(marks_series)
print(type(marks_series))
print(marks_series.shape)
print(marks_series.index)
print(marks_series.values)
print(marks_series.dtypes)
print(marks_series.sum())
print(marks_series.mean())
print(marks_series.max())
print(marks_series.min())
print(marks_series.count())