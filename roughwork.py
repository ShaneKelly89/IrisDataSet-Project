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

#index = ['sepal lenght', 'sepal width', 'petal lenght', 'petal width', 'species']

#I need to get the min and max of each of the 4 variables to plot a histograph 
#Seperate out the each row of data (variable) seperetly 

firstmin = np.min(data[:,0]) #coding for the minumun of the 1st row of data (Septal Lenght)
print(firstmin)
secondmin = np.min(data[:,1]) #sepal width 
print(secondmin)
thirdmin = np.min(data[:,2]) #petal lenght
print(thirdmin)
fourthmin = np.min(data[:,3]) #petal width
print(fourthmin)

#Max for each row of data 
firstmax = np.max(data[:,0]) #Sepal Lenght
print(firstmax)
secondmax = np.max(data[:,1]) #Sepal Width
print(secondmax)
thirdmax = np.max(data[:,2]) #Petal Lenght
print(thirdmax)
fourthmax = np.max(data[:,3]) #Petal Width
print(fourthmax)




