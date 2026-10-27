''' fun_eda_demo
Demonstrate my approach to fun_eda.
'''
import matplotlib.pyplot as plt
import numpy as np
from icecream import ic
from scipy import stats


def custom_mean(in_data):
    ''' Explicitly calculate the mean from a list of numbers '''
    sum_num = np.sum(in_data)
    length_num = len(in_data)
    mean_num = sum_num / length_num
    return mean_num

def descriptive_statistics(in_data, custom_q=None):
    ''' Calculate descriptive statistics for a list of numbers '''
    dict_moments = {
        "first": np.mean(in_data),
        "second": np.var(in_data),
        "third": stats.skew(in_data),
        "fourth": stats.kurtosis(in_data),
    }
    dict_other = {
        "median": np.quantile(in_data, 0.5),
        "percentile_90": np.quantile(in_data, 0.9),
        "percentile_10": np.quantile(in_data, 0.1),
        "maximum": np.max(in_data),
        "minimum": np.min(in_data),
        "standard_deviation": np.std(in_data)
    }
    if custom_q is not None:
        str_custom_percentile = str(np.round(custom_q * 100, 2))
        dict_other["percentile_" + str_custom_percentile] = np.quantile(
            in_data, custom_q)
    return dict_moments, dict_other

def plot_hist(
        in_data, binwidth,
        save_name='/Users/danielhueholt/Documents/Figures/ev228_fig/distribution.pdf'):
    ''' Plot histogram for a list of numbers '''
    ic("Binwidth: " + str(binwidth))
    x_bins = np.arange(
        np.min(in_data) - 2 * binwidth, 
        np.max(in_data) + 2 * binwidth, binwidth)
    val_counts, bin_edges = np.histogram(in_data, x_bins)

    fig, ax = plt.subplots()
    plt.xlabel('value')
    plt.ylabel('counts')
    plot_y = val_counts.astype(float)
    plt.bar(
        bin_edges[:-1], plot_y, edgecolor='#6e7aaa', color=[], width=.3, 
        label='y', linewidth=2, alpha=0.5)
    plt.plot(bin_edges[:-1], plot_y, color='#6e7aaa')
    plt.title('Distribution')
    plt.legend()
    plt.savefig(save_name)

    return fig, ax

def auto_binwidth(in_data):
    ''' Calculate "optimal" binwidth from the Freedman-Diaconis Rule '''
    q75 = np.quantile(in_data, 0.75)
    q25 = np.quantile(in_data, 0.25)
    n = len(in_data)
    optimal = np.round(2 * (q75 - q25) / (n ** (1/3)), 2)

    return optimal