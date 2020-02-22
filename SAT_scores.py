import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

df = pd.read_csv('data/sat_results.csv')


# Ethan printing the info of the dataframe helps us get a better understanding of the data
# We need to know for sure if some of the columns we are reading are in the correct data type, e.g. Score should be a float
# if you noticed the output of info; it says the score columns are object types, which is not valid for calculation 
# or plotting fo charts
na_values1 = df.loc[:, 'SAT Critical Reading Avg. Score'][~(df.loc[:, 'SAT Critical Reading Avg. Score'].str.isnumeric())].unique()
na_values2 = df.loc[:, 'SAT Math Avg. Score'][~(df.loc[:, 'SAT Math Avg. Score'].str.isnumeric())].unique()
na_values3 = df.loc[:, 'SAT Writing Avg. Score'][~(df.loc[:, 'SAT Writing Avg. Score'].str.isnumeric())].unique()
na_values = np.append(na_values1, na_values2)
na_values = np.append(na_values, na_values3)
na_values = np.unique(na_values)
# Ethan to find the non numeric values in a series, i use the function str.isnumeric, this is a dataframe series function
# then i use it to inverse boolean index by using '~' before the criteria to get all the non numeric values
# so i can sift out the values to use as na_values paramter

df = pd.read_csv('data/sat_results.csv', na_values=na_values)

# Ethan: i read the csv file again with the na values


# next step identify the invalid values i want to declare as Missing values, that way the column data type 
# will be maintained as a float type since its all numbers

#Create a stack bar chart for SAT score for different school 

f1 = df[:5][['SCHOOL NAME','SAT Critical Reading Avg. Score','SAT Math Avg. Score','SAT Writing Avg. Score']]
#print(f1)

schools = f1.iloc[:,0]
print(schools)

reading =f1.iloc[:,1]
print(reading)

math = f1.iloc[:,2]
print(math)

writing= f1.iloc [:,3]
print(writing)


plt.figure(figsize =(10,7))

f2=np.arange(len(f1))

reading_graph=plt.bar(x= f2, height=reading, width=0.35)

math_graph=plt.bar(x= f2, height=math, width=0.35, bottom = reading)

writing_graph = plt.bar(x=f2, height=writing, width=0.35, bottom = reading+math)


plt.show()
