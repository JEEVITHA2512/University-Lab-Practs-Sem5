import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.preprocessing import LabelEncoder

fruits=pd.read_csv('fruit.csv')
print('Datatset Summary:')
print(fruits.info())
print("\n First few rows of the dataset:")
print(fruits.head())

label_encoder=LabelEncoder()
fruits['fruit_label']=label_encoder.fit_transform(fruits['fruit_name'])
X=fruits[['mass','width','height','color_score']]
y=fruits['fruit_name']

decision_tree=DecisionTreeClassifier()
decision_tree_scores=cross_val_score(decision_tree,X,y,cv=5)
classifier=tree.DecisionTreeClassifier()
classifier=classifier.fit(X,y)
print(classifier.predict([[210,9.4,6.3,0.6]]))
print('Decision Tree Accuracy(Cross-Validation):',np.mean(decision_tree_scores))

adaboost=AdaBoostClassifier(base_estimator=decision_tree,n_estimators=100)
adaboost_scores=cross_val_score(adaboost,X,y,cv=5)
classifier=tree.DecisionTreeClassifier()
classifier=classifier.fit(X,y)
print(classifier.predict([[210,9.4,6.3,0.6]]))
print('Adaboost(Cross-Validation):',np.mean(decision_tree_scores))
