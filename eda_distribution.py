'''eda_distribution
Carry out exploratory data analysis on a statistical distribution.
'''
import matplotlib.pyplot as plt
import numpy as np
from icecream import ic
from scipy import stats
import math

n_samples_y = 1000
binwidth = 0.5
y = np.random.normal(1.1, 3, size=(n_samples_y,))

#  View a few samples
samples = (y[0], y[np.floor(n_samples_y / 2).astype(int)], y[-1])
ic(samples)

#  Check dimensions
dims = np.shape(y)
ic(dims)

#  Calculate moments of the distribution
first_moment = np.mean(y)
second_moment = np.var(y)
# (In Class) Question 4. Std is approximately equal to the square root of the variance
sqrt_std = math.sqrt(np.std(y))

third_moment = stats.skew(y)
fourth_moment = stats.kurtosis(y)

#(In class) View the four moments
ic(first_moment)
ic(second_moment)
ic(sqrt_std)
ic(third_moment)
ic(fourth_moment)

# (In Class) Question 4. Std is approximately equal to the square root of the variance


#  Calculate other descriptive statistics
median = np.quantile(y, 0.5)
percentile_high = np.quantile(y, 0.9)
percentile_low = np.quantile(y, 0.1)
quantile_closest_2 = np.quantile(y, .9824)
ic(quantile_closest_2)

maximum = np.max(y)
minimum = np.min(y)
standard_deviation = np.std(y)

#(InClass)view other descriptive statistics
ic(median)
ic(percentile_high)
ic(percentile_low)
ic(maximum)
ic(minimum)
ic(standard_deviation)

#In Class Question 5. Create a dictionary that includes all of the statistical moments. 
dict_all_stat_moments = {"Mean" : first_moment , 
                         "Variance" : second_moment , 
                         "Skewness" : third_moment ,
                         "Kurtosis" : fourth_moment
}
ic(dict_all_stat_moments)

dict_non_moment_stats = {"Median" : median ,
                         "Percential High" : percentile_high ,
                         "Percential Low" : percentile_low ,
                         "Maximum" : maximum ,
                         "Minimum" : minimum ,
                         "Standard Deviation" : standard_deviation
}
ic(dict_non_moment_stats)

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

#Adding vertical lines
plt.axvline(median, color = "g" , label = "Median")
plt.axvline(first_moment, color = "r" , label = "Mean")

plt.legend()
plt.savefig('/Users/teddyopler/Desktop/Figures/distribution.pdf')
