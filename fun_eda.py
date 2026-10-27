import math
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from icecream import ic


def mean_calculator(in_list):
    n =  len(in_list)
    sum_y = np.sum(in_list)
    mean = sum_y / n


    return mean

def descriptive_statistics(in_list, q_low=0.1, q_high=0.9):
    n = len(in_list)
    
    sum_in_list = np.sum(in_list)
    first_moment = np.mean(in_list)
    second_moment = np.var(in_list)
    third_moment = stats.skew(in_list, nan_policy='omit')
    fourth_moment = stats.kurtosis(in_list, nan_policy='omit')
    
    median = np.nanquantile(in_list, 0.5)
    percentile_high = np.nanquantile(in_list, q_high)
    percentile_low = np.nanquantile(in_list, q_low)

    dictionary_moments = {
            "Mean" : first_moment, 
            "Variance" : second_moment, 
            "Skewness" : third_moment,
            "Kurtosis" : fourth_moment}
    dictionary_general_stats = {"Number of Samples" : n,
            "Sum" : sum_in_list , "Median" : median,
            "High Percentile" : percentile_high,
            "Low Percentile" : percentile_low}
    return dictionary_moments , dictionary_general_stats

def plot_hist(
        in_list , bin_width,
    save_name = '/Users/teddyopler/Documents/Histogram-DescriptiveStatistics.pdf'):
        ic("Binwidth: " + str(bin_width))
        x_bins = np.arange(
            np.min(in_list) -2 * bin_width,
            np.max(in_list) + 2 * bin_width, bin_width)
        val_counts , bin_edges = np.histogram(in_list , x_bins)
        fig, ax = plt.subplots()
        plt.xlabel('value')
        plt.ylabel('counts')
        plot_y = val_counts.astype(float)
        plt.bar(
            bin_edges[:1], plot_y, edgecolor='#6e7aaa' , color=[], width=.3,
            label='y',linewidth=2,alpha=0.5)
        plt.plot(bin_edges[:-1], plot_y, color='#6e7aaa')
        plt.title('Distribution')
        plt.legend()
        plt.savefig(save_name)

        return fig, ax
def auto_binwidth(in_list):
    q75 = np.nanquantile(in_list, 0.75)
    q25 = np.nanquantile(in_list, 0.25)
    n = len(in_list)
    optimal = np.round(2 * (q75 - q25) / (n ** (1/3)), 2)
    return optimal