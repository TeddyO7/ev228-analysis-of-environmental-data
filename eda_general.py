import fun_eda as fe
import numpy as np
from icecream import ic

in_list = [1,5,10,20,30]
mean_np = np.mean(in_list)
mean_y = fe.mean_calculator(in_list)
ic(mean_y)
ic(mean_np)

descriptive_statistics = fe.descriptive_statistics(in_list, 0.1 , 0.9)
ic(descriptive_statistics)

