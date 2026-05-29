import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('std_data.csv')
print(df.isnull().sum())
sns.heatmap(df.isnull(),cbar=False)
plt.show()
print(f"Avg Age:{df['Age'].mean()}")
print(f"Median of Age:{df['Age'].median()}")
print(f"Mode of Age:{df['Age'].mode()}")
df1=df.drop_duplicates()
print(f'Before cleaning:{df.shape}\nAfter cleaning:{df1.shape}')
