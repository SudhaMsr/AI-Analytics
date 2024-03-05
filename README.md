# AI-Analytics
## Course work


![The palmer penguins](https://github.com/allisonhorst/palmerpenguins/blob/master/man/figures/lter_penguins.png)

# Palmer Penguins

This data is downloaded from [ematm0067](https://github.com/ematm0067/2023_24/tree/main/coursework) As a part of coursework.


> The goal of `palmerpenguins` is to provide a great dataset for data exploration & visualization, as an alternative to iris.
>
> We gratefully acknowledge Palmer Station LTER and the US LTER Network. Special thanks to Marty Downs (Director, LTER Network Office) for help regarding the data license & use.

They've bundled both the raw data and the cleaned data together, which I have also included here.

The main measurements are body mass, culmen (bill) length, bill depth, and flipper length.

### Get the data here

```{r}
# Get the Data

# Read in with tidytuesdayR package 
# Install from CRAN via: install.packages("tidytuesdayR")
# This loads the readme and all the datasets for the week of interest

# Either ISO-8601 date or year/week works!

tuesdata <- tidytuesdayR::tt_load('2020-07-28')
tuesdata <- tidytuesdayR::tt_load(2020, week = 31)

penguins <- tuesdata$penguins

# Or read in the data manually

penguins.csv <- readr::read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-07-28/penguins.csv')

penguins_raw.csv <- readr::read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-07-28/penguins_raw.csv')

```
### Data Dictionary

# `penguins.csv`

|variable          |class   |description |
|:-----------------|:-------|:-----------|
|species           |integer | Penguin species (Adelie, Gentoo, Chinstrap) |
|island            |integer | Island where recorded (Biscoe, Dream, Torgersen) |
|bill_length_mm    |double  | Bill length in millimeters (also known as culmen length) |
|bill_depth_mm     |double  | Bill depth in millimeters (also known as culmen depth) |
|flipper_length_mm |integer | Flipper length in mm |
|body_mass_g       |integer | Body mass in grams |
|sex               |integer | sex of the animal |
|year              |integer | year recorded |

# `penguins_raw.csv`

|variable            |class     |description |
|:-------------------|:---------|:-----------|
|studyName           |character | Study name |
|Sample Number       |double    | Sample id|
|Species             |character | Species of penguin |
|Region              |character | Region where recorded |
|Island              |character | Island where recorded |
|Stage               |character | Stage of egg |
|Individual ID       |character | Individual penguin ID |
|Clutch Completion   |character | Egg clutch completion |
|Date Egg            |double    | Date of egg |
|Culmen Length (mm)  |double    | culmen length in mm (beak length) |
|Culmen Depth (mm)   |double    | culmen depth in mm (beak depth)|
|Flipper Length (mm) |double    | Flipper length in mm |
|Body Mass (g)       |double    | Body mass in g |
|Sex                 |character | Sex of the penguin |
|Delta 15 N (o/oo)   |double    | Blood isotopic Nitrogen - used for dietary comparison |
|Delta 13 C (o/oo)   |double    | Blood isotopic Carbon - used for dietary comparison |
|Comments            |character | Miscellaneous comments |

### Cleaning Script

No cleaning script today, feel free to work with the pre-cleaned data or try your hand at the raw data!


### Understanding Data
-/ Data Exploration is a process of understanding the given data. It gives a chance to get insights and more clarity of data
a. its size and shape
b. data types
### Data preprocessing
a. Cleaning data- removing null values
b. 
### Data Visualisations








