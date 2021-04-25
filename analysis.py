#This is a program created for the purpose of pands 2021 coursework using the Iris Dataset 
#Rough work code for this program was carried out within 'roughwork.py' to allow this program to remain cleaner 
#Author Shane Kelly 

import numpy as np
import pandas as pnd 
import matplotlib.pyplot as plt 
#Importing the needed libraries 
#https://realpython.com/python-csv/

file = "iris.csv"
index = ['sepal length', 'sepal width', 'petal length', 'petal width', 'species']
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

#index = ['sepal length', 'sepal width', 'petal length', 'petal width', 'species']

#http://www.hpc-carpentry.org/hpc-python/03-lists/
#write code and create a variable for each row of data 
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

sepallength = data[:,0]
sepalWidth = data[:,1]
petallength = data[:,2]
petalWidth = data[:,3]
#prints were ran to check to see if the splice was in line with file 

column = [{                              #Creating a dict containing variable and corresponding data 
    "title": "Sepal length",
    "data": sepallength,
},{
    "title": "Sepal Width",
    "data": sepalWidth,
}, {
    "title": "Petal length",
    "data": petallength,
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
    plt.hist(x["data"], color = 'b', label = 'Data')       #creating the histograms within the loop 
    plt.title("Histrogram for {}".format(x["title"]))
    plt.xlabel("{} (cm)".format(x["title"]))
    plt.ylabel("Distribution of occurance")
    plt.legend(loc = 'upper right')
    plt.show()

#Really happy with the above code!! A lot neater and gets rid of un needed lines of repeatative code.

#Having explored and played around with the data, I have decided to create histograms for each of the three species 
#containing the data for each variable 
#To do this I will first isloate the data for each species within the variable columns 
#The use these to create a new variable for each of the 3 species 
#While isolating the data and getting descriptive stats for each was relatively okay, 
#Finding an appropriate way of outputting the descriptives was not so easy for me. 
#The below code took a lot of tinkering and trial and error, but it will provide the min, max, and mean for 
#Sepal Lenght, Sepal Width, Petal Length, and Petal Width for each 3 species of Iris.


#Putting flower data into seperate dicts 
setosa = {'sepal length': data[:50,0], 'sepal width': data[:50,1], 'petal length': data[:50,2], 'petal width': data[:50,3]}
versicolor = {'sepal length': data[50:100,0], 'sepal width': data[50:100,1], 'petal length': data[50:100,2], 'petal width': data[50:100,3]}
virginica = {'sepal length': data[100:,0], 'sepal width': data[100:,1], 'petal length': data[100:,2], 'petal width': data[100:,3]}

#creating new dict to store each flower plus its data
flowers = {'setosa': setosa, 'versicolor': versicolor, 'virginica': virginica}

#https://realpython.com/iterate-through-dictionary-python/
for flower_name, flower_stats in flowers.items():              
    for variable_name, variable_value in flower_stats.items():
        print("The minimum for {} {} is {}".format(flower_name, variable_name, np.min(variable_value)))
        print("The maximum for {} {} is {}".format(flower_name, variable_name, np.max(variable_value)))
        print("The mean for {} {} is {}".format(flower_name, variable_name, np.mean(variable_value)))
        print()
    df = pnd.DataFrame(flower_stats)
    hist = df.hist(bins=8)
    plt.suptitle("Histogram for {}".format(flower_name.capitalize()))
    plt.show()     
#As with the first histograms I tested to see if they could be created within the loop in roughwork 
#Also, as there would be a lot of histograms if I did them all seperately, I wanted to find a way to place
#the four variables for each species in the same output 
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html
#https://www.kite.com/python/docs/matplotlib.figure.Figure.suptitle




#Scatterplots - output a scatteerplot of each pair of variables 
#A scatter plot (also called a scatterplot, scatter graph, scatter chart, scattergram, or scatter diagram) is a 
# type of plot or mathematical diagram using Cartesian coordinates to display values for typically two variables 
# for a set of data

#https://www.w3schools.com/python/python_ml_scatterplot.asp
#https://www.w3schools.com/python/matplotlib_scatter.asp

#Having created a dict and using a loop to create the histograms, I spent time trialing the same for the 
#scatterplots, as similar to previous versions of histrogram code it was very repetative 
#After spending time and with some research and trial and error the below code was written which placed the required 
#information into a dict, which is then looped through using a for loop to output scatterplots for each pair of variables 

#https://stackoverflow.com/questions/30013511/python-plot-a-graph-from-values-inside-dictionary/30013848

scatdict = [{                              #Creating a dict for scatterplot 
    "title": "Sepal length and Sepal Width",
    "labels": ["Sepal length", "Sepal Width"],    #added in labels to use for scatterplot labelling
    "data": [sepallength,sepalWidth]
},{
    "title": "Sepal length and Petal length",
    "labels": ["Sepal length", "Petal length"],
    "data": [sepallength,petallength]
}, {
    "title": "Sepal length and Petal Width",
    "labels": ["Sepal length", "Petal Width"],
    "data": [sepallength,petalWidth]
}, {
    "title": "Sepal Width and Petal length",
    "labels": ["Sepal Width","Petal length"],
    "data": [sepalWidth,petallength]
}, {
    "title": "Sepal Width and Petal Width",
    "labels": ["Sepal Width","Petal Width"],
    "data": [sepalWidth,petalWidth]
}, {
    "title": "Petal length and Petal Width",
    "labels": ["Petal length", "Petal Width"],
    "data": [petallength,petalWidth]
}]

for y in scatdict:                         #for loop to loop through the dict 
    plt.scatter(y["data"][0],y["data"][1], label = "Data")   #calling what info to use for scatterplot (1st entry in 'data' and second entry in 'data)
    plt.title("Scatter Plot for {}.".format(y["title"]))
    plt.xlabel(y["labels"][0])
    plt.ylabel(y["labels"][1])
    plt.legend(loc = 'upper left')
    plt.show()
