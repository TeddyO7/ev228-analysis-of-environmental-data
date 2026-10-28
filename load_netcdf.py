''' load_netcdf
Load a gridded dataset from a netCDF file.
'''
import xarray as xr
from icecream import ic
import matplotlib.pyplot as plt
import numpy as np


#  Import data
ds = xr.load_dataset('/Users/teddyopler/Documents/era5_t2m_202609.nc')
ic(ds)

t2m = ds["t2m"]
ic(t2m)
ic(t2m.dtype)
ic(t2m.attrs)
t2m.plot()
plt.title("2-Meter Air Temperature: First Time Step")
plt.savefig('/Users/teddyopler/Desktop/ev228_figures/era_t2m')
longitude = -104.82
if float(ds.longitude.max()) > 180:
    longitude = longitude % 360

colorado_springs = t2m.sel(
    latitude=38.83,
    longitude = longitude,
    method="nearest"
)
ic(colorado_springs)
ic(colorado_springs.values)

plt.scatter(
    [float(colorado_springs.longitude)],
    [float(colorado_springs.values)]
)
plt.xlabel("Longitude")
plt.ylabel("Temperature (K)")
plt.title("Temperature at the Nearest Grid Point to Colorado Springs")
plt.show()

t2m.isel(time=0).plot()
plt.title("ERA5 Temperature Map: First Time Step")
plt.show()

temperature_data = t2m.data
ic(type(temperature_data))
ic(temperature_data.shape)

flat_temperatures = temperature_data.flatten()
ic(flat_temperatures.shape)

flat_temperatures = flat_temperatures[
    np.isfinite(flat_temperatures)
]

plt.hist(flat_temperatures, bins=30, edgecolor="black")
plt.title("Distribution of ERA5 2-Meter Air Temperatures")
plt.xlabel("Temperature (units from dataset)")
plt.ylabel("Frequency")
plt.show()

ds.close()