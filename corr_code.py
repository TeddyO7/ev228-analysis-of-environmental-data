import pandas as pd
from icecream import ic
import matplotlib.pyplot as plt
import numpy as np
import fun_eda_demo as fed
import scipy.stats as sp

data_nino = pd.read_csv('/Users/teddyopler/Documents/nino34.long.anom.csv')
data_COSair = pd.read_csv('/Users/teddyopler/Documents/COS-Airport_maxT-minT-precip-snow_194801-202212.csv')

minT= data_COSair.loc[ : 'minimumT']
maxT = data_COSair.loc[ :, 'maximumT']
time = data_COSair.loc [: , 'Year_Month']
date_num = time.iloc[1:]
max_temp_num = maxT.iloc[624:902].astype(float)
ic(max_temp_num)

temp_nino = data_nino.loc[ : 'NINA34  missing value -99.99 https://psl.noaa.gov/data/timeseries/month/']
ic(temp_nino)
temp_nino_val = temp_nino.iloc[1560:1837, 1]
ic(temp_nino_val)
date_nino = data_nino.loc[1560:1837 , 'Date']
ic(date_nino)

ic(np.corrcoef(temp_nino_val , max_temp_num))



