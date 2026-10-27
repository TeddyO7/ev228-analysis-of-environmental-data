'''eda_general_demo
Demonstrate my approach to eda_general.
'''
import numpy as np
from icecream import ic

import fun_eda_demo as fed

n_samples_y = 1000
binwidth = 'auto'
normal = np.random.normal(0, 1, size=(n_samples_y,))
gamma = np.random.gamma(3, 1, size=(n_samples_y,))
wald = np.random.wald(3, 5, size=(n_samples_y))
save_folder = '/Users/danielhueholt/Documents/Figures/ev228_fig/'
save_normal = save_folder + 'normal.pdf'
save_gamma = save_folder + 'gamma.pdf'
save_wald = save_folder + 'wald.pdf'

#  View a few samples
normal_samples = (
    normal[0], normal[np.floor(n_samples_y / 2).astype(int)], 
    normal[-1])
gamma_samples = (
    gamma[0], gamma[np.floor(n_samples_y / 2).astype(int)], 
    gamma[-1])
wald_samples = (
    gamma[0], gamma[np.floor(n_samples_y / 2).astype(int)], 
    gamma[-1])
ic(normal_samples, gamma_samples, wald_samples)

#  Check dimensions
normal_dims = np.shape(normal)
gamma_dims = np.shape(gamma)
wald_dims = np.shape(wald)
ic(normal_dims, gamma_dims, wald_dims)

#  Calculate descriptive statistics
normal_stats = fed.descriptive_statistics(normal, custom_q=0.99)
gamma_stats = fed.descriptive_statistics(gamma, custom_q=0.99)
wald_stats = fed.descriptive_statistics(wald, custom_q=0.99)
ic(normal_stats, gamma_stats, wald_stats)

#  Plot histogram
if binwidth == 'auto':
    binwidth_normal = fed.auto_binwidth(normal)
    binwidth_gamma = fed.auto_binwidth(gamma)
    binwidth_wald = fed.auto_binwidth(wald)
else:
    binwidth_normal = binwidth
    binwidth_gamma = binwidth
    binwidth_wald = binwidth
fed.plot_hist(normal, binwidth_normal, save_name=save_normal)
fed.plot_hist(gamma, binwidth_gamma, save_name=save_gamma)
fed.plot_hist(wald, binwidth_wald, save_name=save_wald)