''' probability_distributions
Demonstrate generating and visualizing probability distribution functions.
'''
import matplotlib.pyplot as plt #importing matplotlib.pyplot package.
import numpy as np #importing numpy package.

#  Settings
binwidth = 0.5 #Width of each data point collection group
n_samples_x = 1000 #number of samples on the x axis of the graph
n_samples_y = 1000 #number of samples on the y axis of the graph

x = np.random.normal(0, 1, size=(n_samples_x,)) #x is a random variable that equals a random point on the x-axis
y = np.random.normal(0, 1, size=(n_samples_y,)) #y is a random variable that equals a random point on the y axis

x_bins = np.arange(-4.5, 4.5, binwidth) # x_bins is a variable that has a range of -4.5 - 4.5 and a bin width of 0.5 on the x-axis.
val_counts_x, bin_edges_x = np.histogram(x, x_bins) #all points inside of the x bins creates a histogram with ranges mentioned above from x_bins.
val_counts_y, bin_edges_y = np.histogram(y, x_bins) #describing the y-values 

fig, ax = plt.subplots() 
plt.xlabel('value')
plt.ylabel('counts')
plot_x = val_counts_x.astype(float)
plot_y = val_counts_y.astype(float)
plt.bar(
    bin_edges_x[:-1], plot_x, edgecolor='#b24342', color=[], width=.3, 
    label='x', linewidth=2, alpha=0.5)
plt.bar(
    bin_edges_y[:-1], plot_y, edgecolor='#6e7aaa', color=[], width=.3, 
    label='y', linewidth=2, alpha=0.5)
plt.plot(bin_edges_x[:-1], plot_x, color='#b24342')
plt.plot(bin_edges_y[:-1], plot_y, color='#6e7aaa')
plt.legend()
plt.savefig('/Users/teddyopler/Desktop/Figures/distribution.pdf')