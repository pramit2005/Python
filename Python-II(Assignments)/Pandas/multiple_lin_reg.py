from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import numpy as np
import pandas as pd
df=pd.read_csv('std_data.csv')
df.drop_duplicates()
df=df.dropna()
df1=df[['StudyHours','Age','SleepHours','Attendance']]
df2=df['Marks']
x=df1.to_numpy()
y=df2.to_numpy()
X_train,X_test,y_train,y_test=train_test_split(x,y,random_state=0)
X_train_t=X_train.T
B=np.linalg.inv(X_train_t@X_train)
B=B@(X_train_t@y_train)
y_pred=X_test@B
print(f'Accuracy:{r2_score(y_pred,y_test)}')