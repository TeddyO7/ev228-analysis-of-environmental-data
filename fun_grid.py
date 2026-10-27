'''fun_grid
Functions for gridded data.
'''
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np

def weight_by_latitude(da, latitude):
    ''' Weight gridded data by latitude '''
    weights = np.cos(np.deg2rad(latitude))
    da_weight = da.weighted(weights)

    return da_weight

