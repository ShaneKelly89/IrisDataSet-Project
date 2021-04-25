# IrisDataSet-Project
This is the repository created for the project within PANDS Module 2021. The following statement is the problem statement for the project, as per the breif.\
'This project concerns the well-known Fisher’s Iris data set [3]. You must research the data set
and write documentation and code (in Python [1]) to investigate it. An online search for
information on the data set will convince you that many people have investigated it
previously. You are expected to be able to break this project into several smaller tasks that
are easier to solve, and to plug these together after they have been completed.
You might do that for this project as follows:
1. Research the data set online and write a summary about it in your README.
2. Download the data set and add it to your repository.
3. Write a program called analysis.py that:
• outputs a summary of each variable to a single text file,
• saves a histogram of each variable to png files, and
• outputs a scatter plot of each pair of variables.
It might help to suppose that your manager has asked you to investigate the data set, with a
view to explaining it to your colleagues. Imagine that you are to give a presentation on the
data set in a few weeks’ time, where you explain what investigating a data set entails and how
Python can be used to do it. You have not been asked to create a deck of presentation slides,
but rather to present your code and its output to them.'

# Task Preperation 

For the purpose of this task, the author first created a 'Project Planner' which was used to help guide and manage this project. This planner will have undergone a number of changes through the process of the  project, but will be a constant point of reference throughout. 

Plan for the Project: 

1. Create a repository to be used for the project.
2. Carry out background research on the IRIS Dataset, and write up a concise summary. 
3. Create the appropriate folders to store the required information and data (update and create as the project goes on).
4. Monitor References: Create a word doc to store references throughout the project. Add to Readme near the end.
5. Download the IRIS Dataset.
6. Breakdown the tasks within the project in relation to the investigation of the dataset. Examine the research question, and create a plan on how I intend to investigate the dataset and produce the required outputs.
7. Spent time researching and revising appropriately and wisely. 
8. Make regular and appropriate commits throughout. 

# Background Information 
The Iris Dataset is a multivariate dataset that contains 4 features of 50 samples of three species of the Irish flower, namely _setosa_, _virginica_, and _versicolor_. The 4 features within the dataset are:
1. Lenght of sepal in cm.
2. Width of sepal in cm.
3. Lenght of petal in cm.
4. Width of petal in cm. 

![](Images/Iris.png)

The dataset was first introduced by British statistician, eugenicist, and biologist Ronald Fisher in his 1963 paper '_The use of multiple measurements in taxonomic problems_', which is available to read at <https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-1809.1936.tb02137.x> [1].
The dataset is was introduced as an example of linear discriminant analysis, which refers to 'a method used to find a linear combination of features that characterise or separate two or more classes of objects or events' [2]. As such, based on the combination of the four features mentioned above, Fisher developed a linear discrimination model which was able to distinguish between the three species of Iris. A snapshot of Fisher's original data can be viewed below.\
![](Images/FishersData.png)


# The Environment 
A number of programmes and resources were essential to the completion of this project. This include: _Anaconda_, _Python_, _Visual Studio Code_, _The Iris Dataset_, and _GitHub_.
A selection of Python Library extensions were also utilized throughout. Time was spent becoming familiar with these libraries through both weekly lectures and independent research. The libraries used in this project are: 
* Matplotlib: Matplotlib is a graph plotting library in Python that serves as a visualisation utility. It is a comprehensive library for creating static, animated, and interactive visualisations in Python [3].gi
* NumPy: NumPy is a Python library used for working with arrays. Using NumPy has a number of benefits to data scientists, including increased computational speed, fewer loops, clearer code, and improved quality. It is seen as the de facto standard for multidimensional arrays in Python [4].
* pandas: Pandas is a python library used for working with data sets, and has functions for analysing, cleaning, exploring, and manipulating data. Pandas allows us to analyse big data and make conclusions based on statistical theories [5].


# Exploration of the Data 
Below you will find the results of the exploration of the dataset using Python. As previously mentioned, the code created to run this exploration underwent a number of developments and updates throughout the process.

Based on the background knowledge known about the Iris Dataset, there are certain assumptions that can be made around the data within this dataset. However, the author did not take such assumptions for granted and spent time exploring the data to confirm that the dataset I was using contained the following information before beginning my project: 
1.	That the data contained the correct number of rows and columns (150, 5) 
2.	That I had correctly names the five columns.
3.	That the data contained the three species of flower
4.	That the data was evenly distributed between the three flowers (50 each)

![](Images/IrisdataShapeInfo.png)

![](Images/species.png) 

## Histograms for each variable

As part of the exploration of the dataset code was written to produce Histogram data for each of the following variables: 
1.	Sepal Length 
2.	Sepal Width 
3.	Petal Length 
4.	Petal Width 

To help support and describe the histograms, the minimum, maximum, mean, and standard deviation of each variable were also pulled. 
The first step in getting the above information creating a dict containing each the data and its corresponding data. 

![](Images/dictionary1.png)

Using the above dictionary, a for loop was used to loop through the dictionary data, and output the min, max, mean, and standard deviation of each variable. It was also used to plot and produce the histograms provided below. 

![](Images/loop1.png)

### Sepal Length
The Sepal Length Histogram and the descriptive statistics for Sepal Length are provided below:

![](histograms/SepalLenghtHisto.png)

![](Images/sepallengtdata.png)

As can be seen (add summary)

### Sepal Width

The Sepal Width Histogram and the descriptive statistics for Sepal Width are provided below:

![](histograms/SepalWidthHisto.png)

![](Images/sepalwidthdata.png) 

As can be seen (add summary)


### Petal Length
The Petal Length Histogram and the descriptive statistics for Petal Length are provided below:

![](histograms/PetalLenghtHisto.png)

![](Images/petallengthdata.png)

As can be seen (add summary)


### Petal Width
The Petal Width Histogram and the descriptive statistics for Petal Width are provided below:

![](histograms/PetalWidthHisto.png)

![](Images/petalwidthdata.png)

As can be seen (add summary)

## Histograms for Each Flower
To further investigate the data, separate analysis was carried out for the four variables (sepal length, sepal width, petal length, petal width) for each of the three species Iris flower. The code was developed and improved over the course of the project. 

Firstly, the data for each flower were placed into separate dictionaries, with another dictionary being made storing each flower and its corresponding data: 
![](Images/flowersdict.png)


The code provided above was then used within a for loop to produce the min, mean, and max for each of the four variables per species, while also outputting histograms to visualise the data: 
![](Images/flowerloop.png) 

### Setosa Flower 
Below is a matrix containing histograms for each variable of the Setosa Flower: 
![](histograms/setosahist.png)

and the min, mean, max for each: 

![](Images/setosadata.png) 

### Versicolor Flower 
Below is a matrix containing histograms for each variable of the Versicolor Flower: 
![](histograms/versicolorhist.png)

and the min, mean, max for each: 

![](Images/versicolordata.png) 

### Virginica Flower 
Below is a matrix containing histograms for each variable of the Virginica Flower: 
![](histograms/virginicahist.png)

and the min, mean, max for each: 

![](Images/virginicadata.png) 


## Scatter Plot for each Pair of Variables 
As part of this project we were asked to create scatter plots for each pair of variables. First, a dictionary containing the required information was created. 
![](Images/scatterdict.png)

This dictionary was then used for a loop in which the scatter plots were created. 
![](Images/scatterloop.png)

### Sepal Length and Sepal Width 
Below is a scatter plot of the data for sepal length and sepal width 
![](scatterplots/sepLsepWscatter.png)

Explain ……
### Sepal Length and Petal Length
Below is a scatter plot of the data for sepal length and petal length 
![](scatterplots/sepLpetLscatter.png)

Explain …………..
### Sepal Length and Petal Width
Below is a scatter plot of the data for sepal length and petal width 
![](scatterplots/sepLpetWscatter.png)

Explain …..
### Sepal Width and Petal Length 
Below is a scatter plot of the data for sepal width and petal length 
![](scatterplots/sepWpetLscatter.png)

………….
### Sepal Width and Petal Width
Below is a scatter plot of the data for sepal width and petal width 
![](scatterplots/sepWpetWscatter.png)

……………….
### Petal Length and Petal Width 
Below is a scatter plot of the data for petal length and petal width 
![](scatterplots/petLpetWscatter.png)

…………………..










