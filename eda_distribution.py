'''eda_distribution
Carry out exploratory data analysis on a statistical distribution.
'''
import matplotlib.pyplot as plt
import numpy as np
from icecream import ic
from scipy import stats

n_samples_y = 1000
binwidth = 0.5
y = np.random.normal(0, 1, size=(n_samples_y,))

#  View a few samples
samples = (y[0], y[np.floor(n_samples_y / 2).astype(int)], y[-1])
ic(samples)

#  Check dimensions
dims = np.shape(y)
ic(dims)

#  Calculate moments of the distribution
first_moment = np.mean(y)
second_moment = np.var(y)
third_moment = stats.skew(y)
fourth_moment = stats.kurtosis(y)

#  Calculate other descriptive statistics
median = np.quantile(y, 0.5)
percentile_high = np.quantile(y, 0.9)
percentile_low = np.quantile(y, 0.1)
maximum = np.max(y)
minimum = np.min(y)
standard_deviation = np.std(y)

#  Plot histogram
x_bins = np.arange(-4.5, 4.5, binwidth)
val_counts_y, bin_edges_y = np.histogram(y, x_bins)

fig, ax = plt.subplots()
plt.xlabel('value')
plt.ylabel('counts')
plot_y = val_counts_y.astype(float)
plt.bar(
    bin_edges_y[:-1], plot_y, edgecolor='#6e7aaa', color=[], width=.3, 
    label='y', linewidth=2, alpha=0.5)
plt.plot(bin_edges_y[:-1], plot_y, color='#6e7aaa')
plt.title('Normal distribution')
plt.legend()
plt.savefig('/Users/danielhueholt/Documents/Figures/ev228_fig/distribution.pdf')
