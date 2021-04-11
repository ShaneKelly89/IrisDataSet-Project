#This is a program created for the purpose of pands 2021 coursework using the Iris Dataset 
#Rough work code for this program was carried out within 'roughwork.py' to allow this program to remain cleaner 
#Author Shane Kelly 

import numpy as np
import pandas as pnd 
import matplotlib.pyplot as plt 
#Importing the needed libraries 

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
print("We can also take a look at the statistical summary of the data:")
print(dataset.describe())

#Now I will read the file for NumPy 
data = np.genfromtxt(file, delimiter=',')
print(data)




