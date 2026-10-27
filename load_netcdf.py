''' load_netcdf
Load a gridded dataset from a netCDF file.
'''
import xarray as xr
from icecream import ic

#  Import data
ds = xr.load_dataset('/Users/danielhueholt/Data/ev228_data/gridded/era5_t2m_202609.nc')
