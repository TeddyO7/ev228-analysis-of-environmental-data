''' load_netcdf
Load a gridded dataset from a netCDF file.
'''
#  Import data
import xarray as xr
from icecream import ic
import matplotlib.pyplot as plt
import numpy as np
import fun_eda as fe

# 1. Use ic to view the attributes for the dataset
ds = xr.load_dataset('/Users/teddyopler/Documents/era5_t2m_202609.nc')
ic(ds)
# 2. Use dot or bracket notation to obtain the DataArray
t2m = ds["t2m"]
ic(t2m)
ic(t2m.dtype)
ic(t2m.attrs)
# 3. Use the bound method .plot() to make an initial exploratory figure
t2m.plot()
plt.title("2-Meter Air Temperature: First Time Step")
plt.savefig('/Users/teddyopler/Desktop/ev228_figures/era_t2m.png')
longitude_COS= -104.82
if float(ds.longitude.max()) > 180:
    longitude = longitude_COS % 360
latitude_COS= 38.83
if float(ds.latitude.max()) > 90:
    latitude = latitude_COS % 180

#4. Use sel or isel to extract the latitude/longitude point nearest to Colorado Springs
colorado_springs = t2m.sel(latitude=38.83,longitude = -104.82, method="nearest")
ic(colorado_springs)
ic(colorado_springs.values)


plt.scatter(
    [float(colorado_springs.longitude)],
    [float(colorado_springs.values)]
)
plt.xlabel("Longitude")
plt.ylabel("Temperature (K)")
plt.title("Temperature at the Nearest Grid Point to Colorado Springs")
#plt.show()

# 5. Use .data to obtain the underlying Numpy array
temperature_data = t2m.data
ic(type(temperature_data))
ic(temperature_data.shape)

# 6.Flatten the Numpy array 
arr = np.array(temperature_data)
flatten_array = arr.flatten()
ic(flatten_array)

# 7. Make a histogram of the data
optbin = fe.auto_binwidth(temperature_data)
ic(optbin)
fe.plot_hist(temperature_data, optbin)
ds.close()

#''' 8. Use the updated descriptive statistics function 
# we wrote together to calculate the latitude, longitude,
#  and flat statistics for the dataset'''
dictionary_moments, dictionary_general_stats = fe.descriptive_statistics(t2m, axis='global')
ic(dictionary_moments)
ic(dictionary_general_stats)


# 9. Plot a longitude-averaged statistic of your choice



