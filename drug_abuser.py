import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/drug-abusers-by-major-drugs-of-abuse.csv')
f1 =df[df.loc[:,'year'] > 2015]
#print(f1)
f2 =  f1[f1['status'] == 'Total']
f3 = f2[f2.drug_of_abuse.isin( ['Heroin','Ecstasy','Methamphetamine','Cocaine','Cannabis'])]

#print(f3)

heroin = f3[(f3['drug_of_abuse']=='Heroin')].loc[:, 'no_of_drug_abusers'].reset_index(drop=True)
cannabis = f3[f3['drug_of_abuse']=='Cannabis']['no_of_drug_abusers'].reset_index(drop=True)
methamphetamine = f3[f3['drug_of_abuse']=='Methamphetamine']['no_of_drug_abusers'].reset_index(drop=True)
ecstasy = f3[f3['drug_of_abuse']=='Ecstasy']['no_of_drug_abusers'].reset_index(drop=True)
concaine = f3[f3['drug_of_abuse']=='Cocaine']['no_of_drug_abusers'].reset_index(drop=True)

# Ethan: in your code, when subsetting to get a single column of data from a dataframe
# the original index will be retained, when plotting that data with the index, remember that the x axis ticks 
# by default starts from 0, thus its always easily assumed that the series data has an index from 0, its the case
# for numpy lists or reading fresh data from a csv were new indexes are created. but in data that is extracted from 
# a dataframe, we should be careful about the original indexes, because if the index of your data starts from 265 and 
# your x-axis by default starts from 0, this means the chart will plot the line 265 ticks away...
# to solve this problem, we use the reset_index(drop=True) that will reset the index and drop the old index; why drop=True
# when reset_index, the dataframe will maintain the old index and create a physical column to retain that data,
# but since its not useful, we drop that old index col; therefore drop=True

#print(heroin, cannabis, methamphetamine, ecstasy, concaine)

fig = plt.figure(figsize=(20,7))

ax1 = fig.add_subplot(111)

xlabels = ['2016','2017','2018', '2019']
plt.title('TYPE AND NUMBER OF DRUGS ABUSER FROM 2016 TO 2019')

ax1.plot(heroin, c='b',  label='Heroin', linewidth = 3)
ax1.plot(cannabis, c='r', label='Cannabis',linewidth =3)
ax1.plot(methamphetamine, c= 'g', label='Methamphetamine', linewidth = 3)
ax1.plot(ecstasy, c='y',  label='Ecstasy', linewidth = 3)
ax1.plot(concaine,  c='m', label='Concaine',linewidth =3)

ax1.set_xticks(np.arange(len(xlabels)))
ax1.set_xticklabels(xlabels, rotation=45)

plt.ylabel('Number of Drug Abuser')
plt.xlabel('Year')
plt.grid(True,color='k')
plt.legend(loc='upper right');
