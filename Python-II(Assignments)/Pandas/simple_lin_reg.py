from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import numpy as np
import pandas as pd
df=pd.read_csv('std_data.csv')
df=df.drop_duplicates()
df=df.dropna()
X=df[['StudyHours']].to_numpy()
y=df['Marks'].to_numpy()
X=np.c_[np.ones(X.shape[0]),X]  #Intercept column
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0)
X_train_t=X_train.T
B=np.linalg.inv(X_train_t@X_train)
B=B@(X_train_t@y_train)
y_pred=X_test@B
print(f'Accuracy:{r2_score(y_test,y_pred)}')