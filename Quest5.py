import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics as st

dataset = pd.read_csv('candata.csv')
X = dataset.iloc[:, 0].values
print(X)
#mean,median,mode
mean = np.mean(X)
print("mean is", mean)
median = np.median(X)
print("median is", median)
modex = st.mode(X)
print("mode is", modex)