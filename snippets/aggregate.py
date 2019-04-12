import pandas as pd
import numpy as np

# Load a csv file as a data frame
dat = pd.read_csv("../data/mtcars.csv")
print(dat.head())

# Group by 'cyl' and find the mean of each other column. 
# This creates a new dataframe 
cyl = dat.groupby('cyl').mean()
print(cyl)

# Creates a new data frame that contains gropued rows by 'cyl'
# Prints each dataframe
cyl_groups = dat.groupby('cyl')
for cyl in cyl_groups:
    print("\n---- Rows where 'cyl' is ", cyl[0], "----")
    print(cyl[1])
