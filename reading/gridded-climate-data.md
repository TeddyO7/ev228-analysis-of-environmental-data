# Gridded Climate Data Notes

Gridded climate data refers to data that exists on an x-y grid. In climate applications, the x and y dimensions are often longitude and latitude.  

Examples of gridded environmental data may be familiar because we often see climate data in terms of global maps. For example, the figure below shows a map of annual mean temperature anomalies in 2025 
generated from gridded data in the Berkeley Earth Surface Temperature (BEST) record.
![BEST 2025 temperature anomaly map](/images/BEST-2025-Anomaly-Map.png)

Gridded climate datasets quickly become more complicated! They often vary along many additional dimensions beyond the latitude-longitude grid.
These high-dimensional gridded datasets are discussed more in tomorrow's reading.

## How do we work with gridded climate data?
* The python package `xarray` is designed to work with gridded climate data obtained in the standard netCDF file format.
* `xarray` adds new data structures called `Datasets` and `DataArrays` which attach additional metadata to help use gridded climate data.
* Dimensions in `Datasets` and `DataArrays` are named explicitly: This allows direct reference to the dimension you are interested in through bracket or dot notation.
* For example, for a `Dataset` named `ds` with dimensions `latitude` and `longitude`, the `latitude` dimension could be accessed by either of the following commands:
    * `ds.latitude`
    * `ds['latitude']`
    * e.g., to take the average across the `latitude` dimension, you would write `ds.mean(dim='latitude')`

## Examples of gridded environmental data
* Climate and weather model output
* Reanalysis
* Interpolated observational products
* You may note that these examples usually include at least one more dimension: Time!

## Dimension reduction
* When working with multi-dimensional data, we often want to remove one or more of the dimensions as part of our analysis.
    * For example, think of taking a gridded climate map of temperature and calculating the global mean temperature value.
* Removing a dimension is called *dimension reduction*. Examples include:
    * Calculating any descriptive statistic (e.g., mean, maximum, minimum, etc.)
    * Choosing a single value (often called a *slice*)
    * We will practice these in class on Tuesday.
* When calculating global statistics from latitude and longitude data, you must remember to weight your statistic by latitude.
* Otherwise, your global statistic will be biased by treating all latitudes and longitudes as having the same size. (Latitude/longitude boxes are smaller at the poles than the equator.)
    * `xarray` includes a method to calculate area-weighted statistics.
    * The official `xarray` documentation has a description of this here: [link](https://docs.xarray.dev/en/latest/examples/area_weighted_temperature.html).
    * We will implement this method in class on Tuesday.
 

### Authorship and Acknowledgments
This document was written by Daniel Hueholt.
