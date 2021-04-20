#!/usr/bin/env python
# coding: utf-8

# In[3]:

import pickle as pickle
from scipy import stats
import matplotlib.pyplot as plt
x=[0,1000,2000,3000,4000,5000,6000]
y=[0.625,0.5,0.375,0.1875,0.1,0.0125,0]
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show() 

quality = myfunc(0.2)
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("https://readinglubrigo1.s3.us-east-2.amazonaws.com/Radings.csv")
X = df.iloc[:, 0:1].values
y = df.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)
# Milage=lin_reg.predict([[0.458]])
# print("Milage")
# print(Milage[0])
filename = 'intensity_vs_mileage.sav'
pickle.dump(lin_reg, open(filename, 'wb'))

# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
pol_reg = LinearRegression()
pol_reg.fit(X_poly, y)




def lamda_handler(event,context):
  return event



# Visualizing the Polymonial Regression results
def viz_polymonial():
    plt.scatter(X, y, color='red')
    plt.plot(X, pol_reg.predict(poly_reg.fit_transform(X)), color='blue')
    plt.title('Lubrigo Engine oil quelity tester')
    plt.xlabel('Intensity Ratio')
    plt.ylabel('Milage')
    plt.show()
    return
viz_polymonial()

# Predicting a new result with Polymonial Regression
pol_reg.predict(poly_reg.fit_transform([[0.2]]))
print(quality)


# In[ ]:




