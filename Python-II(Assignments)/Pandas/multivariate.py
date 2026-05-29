import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('std_data.csv')
sns.pairplot(df)
plt.show()
sns.heatmap(df.corr(numeric_only=True),annot=True,cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()