#I will use this space to run descriptive statistics on the dataset 
#Here I will aim to get a further look at the data and use this to report some of the basic stats
#Pandas will be utilised to do so 
#https://www.w3schools.com/python/pandas/default.asp - Link to Pandas info on W3School used throughout 
#https://machinelearningmastery.com/machine-learning-in-python-step-by-step/ also used for reference 

import pandas as pand 

file = "iris.csv"
names = ['sepal lenght', 'sepal width', 'petal lenght', 'petal width', 'species']
dataset = pand.read_csv(file, names = names) #coding for iris.csv 
print("The total number of rows and columns respectively in the Iris Dataset are:",dataset.shape)

print("\n")   #Putting a space between the output so they are not on top of eachother 

print("This is confirmed in the below output:")
print(dataset.info())
print("\n")
print(dataset)
#print(dataset.to_string()) #this will print out the entire dataset if wanted. 

print("\n")

print("The data places variables evenly into three species of Iris Flower:")
print(dataset.groupby('species').size())
 
print("\n")
#we can also get a statistical summary of the dataset 
print("Below is a statistical summary of the data: ")
print(dataset.describe())





