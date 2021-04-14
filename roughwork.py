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
#sl = data[:,0]
#print(sl)
#plt.hist(sl)
#plt.show()
#Sepal Width
#sw = data[:,1]
#print(sw)
#plt.hist(sw)
#plt.show()
#Petal Lenght
#pl = data[:,2]
#print(pl)
#plt.hist(pl)
#plt.show()
#Petal Width
#pw = data[:,3]
#print(pw)
#plt.hist(pw)
#plt.show()

#Create code for each variable first in analysis.py 

#Code added to analysis.py based on rough work here
#Happy with code but it is kind of repetative will look to see if there is a way to make it cleaner? 
#I could try and create a dictionary containing the info about each column 
sepalLenght = data[:,0]
sepalWidth = data[:,1]
petalLenght = data[:,2]
petalWidth = data[:,3]

thisdict = [{
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
for x in thisdict:
    variableMin = np.min(x["data"])   
    variableMax = np.max(x["data"])
    variableMean = np.mean(x["data"])
    variableStd = np.std(x["data"])
    print("The Minimum value for {} is {}".format(x["title"], variableMin))
    print("The Maximum value for {} is {}".format(x["title"], variableMax))
    print("The Mean value for {} is {}".format(x["title"], variableMean))
    print("The Standard Deviation for {} is {}".format(x["title"], variableStd))
    print("\n")
    #trying histogram in the loop?
    plt.hist(x["data"])
    plt.show()
    


#Scatterplots - output a scatteerplot of each pair of variables 
#A scatter plot (also called a scatterplot, scatter graph, scatter chart, scattergram, or scatter diagram) is a 
# type of plot or mathematical diagram using Cartesian coordinates to display values for typically two variables 
# for a set of data

#https://www.w3schools.com/python/python_ml_scatterplot.asp
#https://www.w3schools.com/python/matplotlib_scatter.asp

sepalLenght = data[:,0]
sepalWidth = data[:,1]
petalLenght = data[:,2]
petalWidth = data[:,3]

a = sepalLenght
b = sepalWidth
c = petalLenght
d = petalWidth

plt.scatter(a,b)
plt.title("Scatter Plot for Sepal Lenght and Sepal Width")
plt.xlabel("Sepal Lenght")
plt.ylabel("Sepal Width")
plt.show()
plt.scatter(a,c)
plt.title("Scatter Plot for Sepal Lenght and Petal Lenght")
plt.xlabel("Sepal Lenght")
plt.ylabel("Petal Lenght")
plt.show()
plt.scatter(a,d)
plt.title("Scatter Plot for Sepal Lenght and Petal Width")
plt.xlabel("Sepal Lenght")
plt.ylabel("Petal Width")
plt.show()
plt.scatter(b,c)
plt.title("Scatter Plot for Sepal Width and Petal Lenght")
plt.xlabel("Sepal Width")
plt.ylabel("Petal Lenght")
plt.show()
plt.scatter(c,d)
plt.title("Scatter Plot for Petal Lenght and Petal Width")
plt.xlabel("Petal Lenght")
plt.ylabel("Petal Width")
plt.show()

#Can I do a scatter plot of each 3 of the species of flower?? 
#Seperate the first 50, second 50, 3rd 50 of ?? 

#Setosa flower 
setosaSL = data[:50,0]
setosaSW = data[:50,1]
setosaPL = data[:50,2]
setosaPW = data[:50,3]
#print(setosaSL)pyth
#print(setosaSW)
#print(setosaPL)
#print(setosaPW)
plt.scatter(setosaSL,setosaSW)
plt.show()
#versicolor flower 
versiSL = data[50:100,0]
versiSW = data[50:100,1]
versiPL = data[50:100,2]
versiPW = data[50:100,3]
#print(versiSL)
#print(versiSW)
#print(versiPL)
#print(versiPW)
#verginica 
vergiSL = data[100:,0]
vergiSW = data[100:,1]
vergiPL = data[100:,2]
vergiPW = data[100:,3]
print(vergiSL)
print(vergiSW)
print(vergiPL)
print(vergiPW)
