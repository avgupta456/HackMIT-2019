import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np
import scipy as sci
import pandas as pd

from dataset_map import get_index
from food_predict import get_food_info

import abbrev
import parse
import ocr

import os
import sys

for filename in os.listdir(os.getcwd()+"/DATA"):
    if("jpg" in filename):
        print(filename)
        document = open("Data/"+filename, 'rb')
        data = ocr.getOCR(document)
        [items, prices, total] = parse.getItems(data)

        foods_index = get_index(items)
        food_data = get_food_info(foods_index)
        food_data['price'] = np.array(prices)
        #comment the below lines if you don't want healthy/unhealthy prices
        food_data['healthy_price'] = food_data.loc[food_data['healthy'] == 'yes', 'price'].sum()
        food_data['unhealthy_price'] = food_data.loc[food_data['healthy'] == 'no', 'price'].sum()
        food_data['10_percent_unhealthy'] = food_data["unhealthy_price"]/10
        print(food_data)

        print()
