# AI-Analytics
## Course work

![Penguins](https://github.com/allisonhorst/palmerpenguins/blob/master/man/figures/lter_penguins.png)

# Penguins

This data is downloaded from [ematm0067](https://github.com/ematm0067/2023_24/tree/main/coursework) As a part of coursework.

> The goal of coursework using `penguin data` is to provide a great dataset for data exploration, visualization & predicting the penguin type.
>
> 

The main measurements are body mass, culmen (bill) length, bill depth, and flipper length.

### Get the data 

```{r}
# Reading the data manually
penguins.csv <- readr::read_csv('https://github.com/SudhaMsr/AI-Analytics/blob/main/penguins.csv')
```

## Understanding the Data
It is important to understand the data before doing analysis as it gives an overview of the dataset. Understanding the given columns and finding the relationships and getting insights from the data.

#### My dataset consisted of the following information:

# `penguins.csv`

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

#### Few basic findings from dataset:
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








