import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy as sci
import pandas as pd
from dataset_map import get_index
from food_predict import get_food_info

data = [['grapefruit juice'],[]]
foods_index = get_index(data[0])
food_data = get_food_info(foods_index)
print(food_data)
