'''count_outcomes
Count outcomes for rolling a virtual die. Used to demonstrate fundamental 
probability concepts.
'''
import random

import matplotlib.pyplot as plt
import numpy as np
from icecream import ic

import fun_probability as fp

#  Demonstrate rolling a single virtual die
roll_value = random.randint(1, 6)
roll_message = 'One dice roll: ' + str(roll_value)
ic(roll_message)

#  Roll many times
list_rolls = fp.dice_roll(n_sides=6, n_rolls=30000)
str_all_rolls = 'All rolls: ' + str(list_rolls)
num_rolls = len(list_rolls)
str_num_rolls = 'Number of rolls: ' + str(num_rolls)
ic(str_all_rolls)
ic(str_num_rolls)

#  Plot counts of each value
x_bins = np.arange(1, 7)
val_counts, bin_edges = np.histogram(list_rolls, bins=6, range=(1, 6))

fig, ax = plt.subplots()
ax.bar(x_bins, val_counts, color='#6e7aaa')
plt.xlabel('Possible values', fontsize=14)
plt.xticks(fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.yticks(fontsize=14)
plt.title('Counts of each value from rolling die')
plt.savefig('/Users/teddyopler/Desktop/Figures/dice_roll_30000.pdf')