''' station_load_csv
Load a timeseries from a weather station CSV file.
'''
import pandas as pd
from icecream import ic
import matplotlib.pyplot as plt
import numpy as np
import fun_eda as fe

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

#ic(df)
#ic(df_head)
#ic(df_tail)
#ic(df.columns)
#ic(minT)
#ic(maxT)

descriptive_stats = fe.descriptive_statistics(max_temp_num , 0.1 , 0.9)
ic(descriptive_stats)

ic(fe.auto_binwidth(max_temp_num))
ic(fe.plot_hist(max_temp_num,6.11))


#making a graph/figure
fig = plt.subplot()
plt.xlabel('Time', fontsize=14)
plt.ylabel(' Max Temperature (F)', fontsize=14)
plt.scatter(np.arange (0,len(date_num)), max_temp_num) 
plt.title('Max and Min Temperatures (F) from 01-2022 -- 12-2022')
plt.savefig('/Users/teddyopler/Documents/COS-Airport_maxT-minT-precip-snow_194801-202212.pdf')

#making histogram


