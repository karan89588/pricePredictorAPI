import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
import pickle

dataset=pickle.load(open('trainabledata.pickle','rb'))
data2=dataset['data']
labels=dataset['labels']

print(data2)
print(labels)

Xtrain,Xtest,Ytrain,Ytest=train_test_split(data2,labels,test_size=0.2,random_state=2)
regr=RandomForestRegressor(max_depth=1000,random_state=0)
regr.fit(Xtrain,Ytrain)

y_pred=regr.predict(Xtest)
r2_score(Ytest,y_pred)

filename='price_predictor_veg.pickle'
pickle.dump(regr,open(filename,'wb'))