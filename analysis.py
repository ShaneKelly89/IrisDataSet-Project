#This is a program created for the purpose of pands 2021 coursework using the Iris Dataset 
#Rough work code for this program was carried out within 'roughwork.py' to allow this program to remain cleaner 
#Author Shane Kelly 

import numpy as np
import pandas as pnd 
import matplotlib.pyplot as plt 
#Importing the needed libraries 
#https://realpython.com/python-csv/

file = "iris.csv"
index = ['sepal lenght', 'sepal width', 'petal lenght', 'petal width', 'species']
dataset = pnd.read_csv(file, names = index) 
#Importing and coding the data 

#Below are the descriptive statistics for the dataset using pandas 
#https://www.w3schools.com/python/pandas/default.asp
#https://machinelearningmastery.com/machine-learning-in-python-step-by-step/ 

print("\n")
print("The total number of rows and columns respectively in the Iris Dataset are:",dataset.shape)  
print("This is confirmed in the below output:")
print(dataset.info())
print(dataset)
#print(dataset.to_string()) #this will print out the entire dataset if wanted. 
print("\n")
print("The data places variables evenly into three species of Iris Flower:")
print(dataset.groupby('species').size())
print("\n")
#Now I will read the file for NumPy 
#https://stackoverflow.com/questions/3518778/how-do-i-read-csv-data-into-a-record-array-in-numpy
data = np.genfromtxt(file, delimiter=',')
#print(data)

#index = ['sepal lenght', 'sepal width', 'petal lenght', 'petal width', 'species']

#http://www.hpc-carpentry.org/hpc-python/03-lists/
#I will now write code and create a variable for each row of data 


sepalLenght = data[:,0]
sepalWidth = data[:,1]
petalLenght = data[:,2]
petalWidth = data[:,3]
#print(sepalLenght)
#print(sepalWidth)
#print(petalLenght)
#print(petalWidth)
#ran to check to see if the splice was in line with file 

#taking a closer look at each of the variables 
#lets use python to describe the statistical properties of each variable 
#https://jakevdp.github.io/PythonDataScienceHandbook/02.04-computation-on-arrays-aggregates.html
#with our newly created variables above we can run stats for the min, max, mean, and st. dev for each 

print("As seen above, the dataset contains numeric data which is held within four seperate columns")
#Sepal Lenght stats 
print("Below are some statistics of the 'Sepal Lenght' column within the dataset")
slMin = np.min(sepalLenght)
print("Sepal Lenght minimum:",slMin)
slMax = np.max(sepalLenght)
print("Sepal Lenght max:",slMax)
slMean = np.mean(sepalLenght)
print("Sepal Lenght mean:",slMean)
slStd = np.std(sepalLenght)
print("Sepal Lenght standard deviation:",slStd)

print("\n")
#Sepal Width stats 
print("Below are some statistics of the 'Sepal Width' column within the dataset")
swMin = np.min(sepalWidth)
print("Sepal Width min:",swMin)
swMax = np.max(sepalWidth)
print("Sepal Width max:",swMax)
swMean = np.mean(sepalWidth)
print("Sepal With mean:",swMean)
swStd = np.std(sepalWidth)
print("Sepal Width standard deviation:",swStd)

print("\n")
#Petal Lenght stats
print("Below are some statistics of the 'Petal Lenght' column within the dataset")
plMin = np.min(petalLenght)
print("Petal Lenght minimum:",plMin)
plMax = np.max(petalLenght)
print("Petal Lenght max:",plMax)
plMean = np.mean(petalLenght)
print("Petal Lenght mean:",plMean)
plStd = np.std(petalLenght)
print("Petal Lenght standard deviation:",plStd)

print("\n")
#Petal Width stats
print("Below are some statistics of the 'Petal Width' column within the dataset")
pwMin = np.min(petalWidth)
print("Petal Width min:",pwMin)
pwMax = np.max(petalWidth)
print("Petal Width max:",pwMax)
pwMean = np.mean(petalWidth)
print("Petal With mean:",pwMean)
pwStd = np.std(petalWidth)
print("Petal Width standard deviation:",pwStd)