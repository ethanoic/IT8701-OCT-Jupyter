import pandas as pd

# Ethan: in read_csv, you can use no_values to tell pandas what are considered NaN or missing values, 
# this is important because if not declared, the column like price which needs to be processed as a float type
# will not be usable, thus the statistical functions cannot be applied to that column

df = pd.read_csv('data/median-resale-prices-for-registered-applications-by-town-and-flat-type.csv',
                na_values=['na','-'])

#print(df)
df1 = df[['quarter','flat_type', 'price']]
#print(df1)
re2018 = '^2018'
df2 = df1[df1['quarter'].str.contains(re2018)]
#print(df2)
# df3 = df2.replace('na',0)
# df4 = df3.replace('-', 0)
# print(df4)

df_5room = df4[df4['flat_type']=='5-room']

# Ethan: its probably ok to just filter out the 5 rooms for calculations here, no need to extract the price
print('4 room mean price: ${:2f}'.format(df4[df4['flat_type']=='4-room']['price'].mean()))

# Ethan: the mean function is a dataframe function that can be applied using iloc or loc to subset the columns
print('5 room mean price: ${:2f}'.format(df_5room.loc[:, 'price'].mean()))

#df6 = df['df5'].mean()
#print(df6)
