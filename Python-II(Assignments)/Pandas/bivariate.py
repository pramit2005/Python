import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('std_data.csv')
plt.scatter(df['StudyHours'], df['Marks'])
plt.xlabel('StudyHours')
plt.ylabel('Marks obtained')
plt.title('Study vs Marks')
plt.show()
corr=df.corr(numeric_only=True)
print(corr)