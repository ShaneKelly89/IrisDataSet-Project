#I will use this space to run descriptive statistics on the dataset 
#Here I will aim to get a further look at the data and use this to report some of the basic stats
#Pandas will be utilised to do so 
#https://www.w3schools.com/python/pandas/default.asp - Link to Pandas info on W3School used throughout 
#https://machinelearningmastery.com/machine-learning-in-python-step-by-step/ also used for reference 

import pandas as pand 

file = "iris.csv"
dataset = pand.read_csv(file) #coding for iris.csv 
#print(dataset.shape)
print(dataset.info())


print("The total number of rows and columns respectively in the Iris Dataset are:",dataset.shape)

#print(dataset.to_string()) #this will print out the entire dataset if wanted. 
print("This is confirmed in the below output:")
print(dataset)

#we can also get a statistical summary of the dataset 
print("Below is a statistical summary of the data: ")
print(dataset.describe())





