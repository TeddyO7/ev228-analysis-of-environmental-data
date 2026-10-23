'''trials_needed_for_value
Obtain the frequency for a given value based on the number of trials.
'''
import matplotlib.pyplot as plt
import numpy as np
from icecream import ic

import fun_probability as fp

list_trials = [100, 1000, 10000, 30000]
list_val_perc = []
for loop_trials in list_trials:
    dict_perc, out_val = fp.dice_value_trials(n_rolls=loop_trials, value_oi=1)
    list_val_perc.append(out_val)
ic(list_val_perc)

expect_perc = 1 / 6 * 100
x_limits = [1000, 30000]

fig, ax = plt.subplots()
plt.plot(list_trials, list_val_perc, color='#6e7aaa', linewidth=3)
plt.plot(x_limits, [expect_perc, expect_perc], color='r')
plt.xlabel('Number of trials', fontsize=14)
plt.xticks(fontsize=14)
plt.xlim(x_limits)
plt.ylabel('Percent frequency', fontsize=14)
plt.yticks(fontsize=14)
plt.title('Frequency of obtaining a value by number of trials')
plt.savefig('/Users/teddyopler/Desktop/Figures/trials_needed_for_value_different_x_limit_and_list_trials.pdf')