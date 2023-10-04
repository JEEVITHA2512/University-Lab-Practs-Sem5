import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

col_names=['pregnant','glucose','bp','skin','insulin','bmi','pedigree','age','label']
pima=pd.read_csv('diabetes.csv',header=None,names=col_names)
feature_cols=['pregnant','insulin','bmi','age','glucose','bp','pedigree']

X=pima[feature_cols]
y=pima.label

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=1)
df=pd.read_csv('diabetes.csv')

x=df.drop('Outcome',axis=1)
y=df['Outcome']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)

model=DecisionTreeClassifier()
model.fit(X_train,y_train)
Y_pred=model.predict(X_test)

if model.predict([[1,85,66,29,0,26.6,0.351,31]])[0]==1:
    print("Having diabetics")
else:
    print('Not having diabetics')

pima.head()

