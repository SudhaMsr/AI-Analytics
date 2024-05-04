<h1 align="center"> Introduction to AI and Text Analytics - EMATM0067</h1>
<h1 align="center">AI Coursework on Palmer Penguins Dataset</h1>

## Overview:
This repository contains the coursework for the ***Introduction to AI*** course. 

Coursework involves a thorough analysis of the Palmer Penguins dataset, focusing on predicting the species type based on physical characteristics. The dataset, provides a unique opportunity to apply machine learning techniques to ecological data. This analysis not only aims to accurately predict penguin species but also to explore the data with care, emphasizing the process over the final accuracy metrics.


<div align="center">
  <img src="https://github.com/SudhaMsr/AI-Analytics/blob/main/penguins.jfif" alt="Penguins" width="500">
These are the types of penguins, I am working on.
</div>

# Project Overview 
## Question 1:
### Task:
#### Explore the penguin.csv dataset to predict the penguin type using the Penguins dataset. This involves data visualization and algorithm selection.

### Understanding the Data  
1. The data used for this project is the [penguin.csv](https://github.com/ematm0067/2023_24/blob/main/coursework/penguins.csv) dataset
2. Get the from [penguin.csv](https://github.com/ematm0067/2023_24/blob/main/coursework/penguins.csv)
   - It contains information about penguins of three different types. 
   - It is important to understand the data before doing analysis as it gives an overview of the dataset. Understanding the 
     given columns and finding the relationships and getting insights from the data.
3. The main measurements are body mass, culmen (bill) length, bill depth, and flipper length.

### Dataset consisted of the following information
#### The penguin dataset contains observations of penguins with the following attributes:

|variable          |class   |description |
|:-----------------|:-------|:-----------|
|rowid             |integer | Serial number
|species           |integer | Penguin species (Adelie, Gentoo, Chinstrap) |
|island            |integer | Island where recorded (Biscoe, Dream, Torgersen) |
|bill_length_mm    |double  | Bill length in millimeters (also known as culmen length) |
|bill_depth_mm     |double  | Bill depth in millimeters (also known as culmen depth) |
|flipper_length_mm |integer | Flipper length in mm |
|body_mass_g       |integer | Body mass in grams |
|sex               |integer | sex of the animal |
|year              |integer | year recorded |

3. The main measurements are body mass, culmen (bill) length, bill depth, and flipper length.

### Basic findings from dataset (Using Exploratory Data Analysis):
Explore the given [penguin.csv](https://github.com/ematm0067/2023_24/blob/main/coursework/penguins.csv) dataset. 
And some basic checks:
   a. Structure of the data
   b. Number of rows and columns
   c. Data types of each column (Integer, String, Bool, Float, etc..)
   d. Understanding the context of the data  

## Data Analysis:
After understanding the basic details of dataset, next step is to analyse and exploring the data.
a. It includes teh summary of mathematical(Statistical) data such as Mean, Median, Mode, Percentile data, etc..

## Data Visualisation:
#### Why Visualisation?
a. Visualization helps in understanding data patterns and trends (Human readable). It help the people to analyzing data, even if they are not from technical background. Plots and other visualization diagrams enable better decision-making by providing a visual context for data. Interactivity is crucial to handle complex data.

b. Easy to measure accuracy and to scale.

c. It helps the user to solve a problem or understand a challenge, not to draw a picture.

#### Why in diagrams?
a. Visualisation tool is the best for data exploration. Visualising the data through various graphs and plots from [Matplotlib](https://matplotlib.org/stable/plot_types/index.html) , [Seaborn](https://seaborn.pydata.org/tutorial/introduction.html) and Python libraries.

#### Why Color coding?
a. Color coding can helps in identify patterns, trends, or outliers within the data and explore relationships between variables.
 

### Data preprocessing
a. Cleaning data- removing null values

b. 
### Data Visualisations



### Question 2:
Addressing ethical challenges in data science and AI.



references:

https://allisonhorst.github.io/palmerpenguins/articles/examples.html
https://allisonhorst.github.io/palmerpenguins/articles/intro.html
https://learn.microsoft.com/en-gb/training/modules/fundamentals-machine-learning/6-multiclass-classification
https://learn.microsoft.com/en-gb/training/modules/fundamentals-machine-learning/8-deep-learning
