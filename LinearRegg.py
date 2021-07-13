# -*- coding: utf-8 -*-
"""
Created on Tue May 25 00:22:39 2021

@author: Nachiketu
"""
#function for Mean calculation:
def mean(x):
    total = 0
    for i in list(x):
        total = total + i
    mean = (1/len(x) * total)
    return mean

#function for Summation calculation:
def summation(x):
    summation = 0
    for i in list(x):
        summation = summation + i
    return summation


#Main Program begins from here:

x = [1,2,4,3,5]
y = [1,3,3,2,5]
print('x: ',x)
print('y: ',y)

#calculation of mean x & y:
print('mean of x: ', mean(x))
print('mean of y: ', mean(y))

#calculation of error x & y with respective means x & y:
errx = [(x[i] - mean(x)) for i in range(len(x))]
erry = [(y[i] - mean(y)) for i in range(len(y))]

#Multiplication of error x & y:
mul = [(errx[i] * erry[i]) for i in range(len(x))]

#squaring of each error x value:
sqx = [pow(errx[i],2) for i in range(len(x))]


#calculation of B1:
b1 = summation(mul) / summation(sqx)
print('B1: ', b1)

#calculation of B0:
b0 = mean(y) - b1 * mean(x)
print('B0: ',b0)

#Prediction of y from the formula:
predy = [(b0+b1*i) for i in list(x)]
print('Formula used for Prediction of y: y = B0 + B1 * x')
print('Predicted y: ', predy)
print('Actual y: ', y)

#Plotting the values of x v/s y & x v/s predicted y:
import matplotlib.pyplot as plt

plt.plot(x, y,'ro')
plt.plot(x, predy,'ob')
plt.plot(x, predy)
plt.show()

#calculation of RMSE numerator & denominator:
rmsenum = [(predy[i] - y[i]) for i in range(len(y))]
rmsesq = [pow(rmsenum[i],2) for i in range(len(rmsenum))]

#calculation of Root Mean Squared Error:
import math
rmse = math.sqrt(summation(rmsesq) / len(rmsenum))
print('Root Mean Squared Error: ',rmse)