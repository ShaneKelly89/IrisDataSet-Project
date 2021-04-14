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
#I will also plot each variable on a histrgram 
#https://bit.ly/325l7aw


#Having looked back over previous lectures and searching online for a way to tidy up my code 
#I tried creating a dict which would hold the variable title and its assocaited data
#Rough work was carried out in roughwork.py
#https://learnonline.gmit.ie/pluginfile.php/293981/mod_label/intro/Lab%2005%20dataStructures.pdf 
#https://jakevdp.github.io/WhirlwindTourOfPython/06-built-in-data-structures.html

print("As seen above, the dataset contains numeric data which is held within four seperate columns")
print("Printed blew are some statistical details for each of the four variables in the columns:")

column = [{                              #Creating a dict containing variable and corresponding data 
    "title": "Sepal Lenght",
    "data": sepalLenght,
},{
    "title": "Sepal Width",
    "data": sepalWidth,
}, {
    "title": "Petal Lenght",
    "data": petalLenght,
}, {
    "title": "Petal Width",
    "data": petalWidth,
}]
for x in column:                   #creating a for loop to go through our dict 
    variableMin = np.min(x["data"])   #creating varaibles to loop through 
    variableMax = np.max(x["data"])
    variableMean = np.mean(x["data"])
    variableStd = np.std(x["data"])
    print("The Minimum value for {} is {}".format(x["title"], variableMin))
    print("The Maximum value for {} is {}".format(x["title"], variableMax))
    print("The Mean value for {} is {}".format(x["title"], variableMean))
    print("The Standard Deviation for {} is {}".format(x["title"], variableStd))
    print("\n")


#Histograms
plt.hist(sepalLenght, color = 'b', label = 'Data')
plt.legend()       
plt.title("Histrogram for Sepal Lenght Data")
plt.xlabel('Sepal Lenght (cm)')
plt.ylabel('distribution of occurance')
plt.show()

plt.hist(sepalWidth, color = 'b', label = 'Data')
plt.legend()       
plt.title("Histrogram for Sepal Width Data")
plt.xlabel('Sepal Width (cm)')
plt.ylabel('distribution of occurance')
plt.show()

plt.hist(petalLenght, color = 'b', label = 'Data')
plt.legend()       
plt.title("Histrogram for Petal Lenght Data")
plt.xlabel('Petal Lenght (cm)')
plt.ylabel('distribution of occurance')
plt.show()

plt.hist(petalWidth, color = 'b', label = 'Data')
plt.legend()       
plt.title("Histrogram for Petal Width Data")
plt.xlabel('Petal Width (cm)')
plt.ylabel('distribution of occurance')
plt.show()

#Happy with code at this point, will start looking at scatterplots now but will also be checking if code can improve
#Refer to line 70 in roughwork.py

#Scatterplots - output a scatteerplot of each pair of variables 
#A scatter plot (also called a scatterplot, scatter graph, scatter chart, scattergram, or scatter diagram) is a 
# type of plot or mathematical diagram using Cartesian coordinates to display values for typically two variables 
# for a set of data

#https://www.w3schools.com/python/python_ml_scatterplot.asp
#https://www.w3schools.com/python/matplotlib_scatter.asp

a = sepalLenght        #creating variables to use for scatterplots 
b = sepalWidth
c = petalLenght
d = petalWidth

plt.scatter(a,b, color = 'r')
plt.title("Scatter Plot for Sepal Lenght and Sepal Width")
plt.xlabel("Sepal Lenght")
plt.ylabel("Sepal Width")
plt.show()
plt.scatter(a,c, color = 'r')
plt.title("Scatter Plot for Sepal Lenght and Petal Lenght")
plt.xlabel("Sepal Lenght")
plt.ylabel("Petal Lenght")
plt.show()
plt.scatter(a,d, color = 'r')
plt.title("Scatter Plot for Sepal Lenght and Petal Width")
plt.xlabel("Sepal Lenght")
plt.ylabel("Petal Width")
plt.show()
plt.scatter(b,c, color = 'r')
plt.title("Scatter Plot for Sepal Width and Petal Lenght")
plt.xlabel("Sepal Width")
plt.ylabel("Petal Lenght")
plt.show()
plt.scatter(c,d, color = 'r')
plt.title("Scatter Plot for Petal Lenght and Petal Width")
plt.xlabel("Petal Lenght")
plt.ylabel("Petal Width")
plt.show()
