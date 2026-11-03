''' station_load_csv
Load a timeseries from a weather station CSV file.
'''
import pandas as pd
from icecream import ic
import matplotlib.pyplot as plt
import numpy as np
import fun_eda_demo as fed
import scipy.stats as sp

#dataframe
df = pd.read_csv('/Users/teddyopler/Documents/COS-Airport_maxT-minT-precip-snow_194801-202212.csv')
#exploring  bounds and extracting quantities
minT= df.loc[ : 'minimumT']
maxT = df.loc[ :, 'maximumT']
time = df.loc [: , 'Year_Month']
date_num = time.iloc[1:]
max_temp_num = maxT.iloc[1:].astype(float)

df_head = df.head()
df_tail = df.tail()

ic(df)
ic(df_head)
ic(df_tail)
ic(df.columns)
ic(minT)
ic(maxT)

descriptive_stats = fed.descriptive_statistics(max_temp_num , None)
ic(descriptive_stats)

ic(fed.auto_binwidth(max_temp_num))
fed.plot_hist(max_temp_num,6.11)


#making a graph/figure
fig = plt.subplot()
plt.xlabel('Time', fontsize=14)
plt.ylabel(' Max Temperature (F)', fontsize=14)
plt.scatter(np.arange (0,len(date_num)), max_temp_num) 
plt.title('Max and Min Temperatures (F) from 01-2022 -- 12-2022')
ic(sp.linregress(np.arange(len(date_num)), max_temp_num, nan_policy='omit'))
plt.axline(xy1=(0, 61.50477396960508), slope=0.0027097413879332627)
ic(sp.theilslopes(max_temp_num , x=None , alpha=.95, method='separate', axis=None , nan_policy='omit' , keepdims=False))
#plt.axline(xy1())
plt.savefig('/Users/teddyopler/Documents/COS-Airport_maxT-minT-precip-snow_194801-202212_linreg.pdf')

#making histogram



