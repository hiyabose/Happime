#  Import all the libraries for predictive modelling

import numpy as np #create arrays
import pandas as pd
import matplotlib.pyplot as plt #plot data
import seaborn as sns #plot data
import missingno as ms #plot missing data
#  Data Cleaning
url2='https://raw.githubusercontent.com/hiyabose/Depression/master/newsurvey.csv'
df = pd.read_csv(url2)
df.head()
df.info()
ms.matrix(df)
df.max()
df.describe()
df.shape
sns.swarmplot(y="Age", x=" Risk", data=df)
plt.show()
"""Here also we can see that the majority are depressed in their mid life."""
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
df.info()
train = df.drop(['Name','score',' Risk','Age'], axis=1)
train= np.asarray(train, dtype='float64')
test = df[[' Risk']]
test= np.asarray(test, dtype='float64')
test.shape
X_train, X_test, y_train, y_test = train_test_split(train,test, test_size=0.3, random_state=2)
reg = LogisticRegression()
reg.fit(X_train, y_train)
pred = reg.predict(X_test)
pred
n =[[0,1,1,0]]
o = reg.predict(n)
o
pred.shape
reg.score(X_test, y_test)
X_test.shape
"""Accuracy rate 77.77% we can say :)"""
import pickle
pickle.dump(reg,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))
