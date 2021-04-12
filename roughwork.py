#This is a space where I will work on the code to complete the task 
#When I feel the code is working well, I will transfer it to 'analysis.py' which is the main code space. 
#Write a program called analysis.py that:
#  outputs a summary of each variable to a single text file,
#• saves a histogram of each variable to png files, and
#• outputs a scatter plot of each pair of variables. 

#What are the variables? 
#What do I need to create a histogram of the variables 
#What do I need to create scatter plot of each pair (what does 'pair' mean?) of variables
#https://realpython.com/python-csv/
import numpy as np
import pandas as pnd 
import matplotlib.pyplot as plt 

#https://stackoverflow.com/questions/3518778/how-do-i-read-csv-data-into-a-record-array-in-numpy

file = "iris.csv"
data = np.genfromtxt(file, delimiter=',')
#print(data)

#index = ['sepal lenght', 'sepal width', 'petal lenght', 'petal width', 'species']

#Seperate out the each row of data (variable) seperetly 
#Min and max for each variable 
firstmin = np.min(data[:,0]) #coding for the minumun of the 1st row of data (Septal Lenght)
#print(firstmin)
secondmin = np.min(data[:,1]) #sepal width 
#print(secondmin)
thirdmin = np.min(data[:,2]) #petal lenght
#print(thirdmin)
fourthmin = np.min(data[:,3]) #petal width
#print(fourthmin)

#Max for each row of data 
firstmax = np.max(data[:,0]) #Sepal Lenght
#print(firstmax)
secondmax = np.max(data[:,1]) #Sepal Width
#print(secondmax)
thirdmax = np.max(data[:,2]) #Petal Lenght
#print(thirdmax)
fourthmax = np.max(data[:,3]) #Petal Width
#print(fourthmax)

#Trying at plotting historgrams 
#Septal Lenght
sl = data[:,0]
print(sl)
plt.hist(sl)
plt.show()
#Sepal Width
sw = data[:,1]
print(sw)
plt.hist(sw)
plt.show()
#Petal Lenght
pl = data[:,2]
print(pl)
plt.hist(pl)
plt.show()
#Petal Width
pw = data[:,3]
print(pw)
plt.hist(pw)
plt.show()

#Create code for each variable first in analysis.py 

#Code added to analysis.py based on rough work here
#Happy with code but it is kind of repetative will look to see if there is a way to make it cleaner? 
