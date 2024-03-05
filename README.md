# AI-Analytics
## Course work

![Penguins](https://github.com/allisonhorst/palmerpenguins/blob/master/man/figures/lter_penguins.png)

# Penguins

This data is downloaded from [ematm0067](https://github.com/ematm0067/2023_24/tree/main/coursework) As a part of coursework.

> The goal of `penguin data` is to provide a great dataset for data exploration, visualization & predicting the penguin type.
>
> 

The main measurements are body mass, culmen (bill) length, bill depth, and flipper length.

### Get the data here

```{r}
# Get the Data

# read the data manually

penguins.csv <- readr::read_csv('https://github.com/SudhaMsr/AI-Analytics/blob/main/penguins.csv')

```
### Data Dictionary

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



### Understanding Data
-/ Data Exploration is a process of understanding the given data. It gives a chance to get insights and more clarity of data
a. its size and shape
b. data types
### Data preprocessing
a. Cleaning data- removing null values
b. 
### Data Visualisations








