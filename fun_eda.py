import math
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


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
    third_moment = stats.skew(in_list)
    fourth_moment = stats.kurtosis(in_list)
    median = np.quantile(n, 0.5)
    percentile_high = np.quantile(n, q_high)
    percentile_low = np.quantile(n, q_low)

    dictionary = {"Mean" : first_moment, 
            "Variance" : second_moment, 
            "Skewness" : third_moment,
            "Kurtosis" : fourth_moment,
            "Median" : median,
            "High Percentile" : percentile_high,
            "Low Percentile" : percentile_low
}
    return dictionary





    