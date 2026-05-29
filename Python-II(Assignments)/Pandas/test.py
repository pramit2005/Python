import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('index.csv')
df1=df.drop_duplicates()
plt.hist(df1)
plt.show()