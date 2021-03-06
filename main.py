import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np
import scipy as sci
import pandas as pd

from helper.dataset_map import get_index
from helper.food_predict import get_food_info

from helper import abbrev
from helper import parse
from helper import ocr

import os
import sys

for filename in os.listdir(os.getcwd()+"/data/data_jpg"):
    if("jpg" in filename):
        print(filename)
        document = open("data/data_jpg/"+filename, 'rb')
        data = ocr.getOCR(document)
        [items, prices, total] = parse.getItems(data)

        foods_index = get_index(items)
        food_data = get_food_info(foods_index)
        food_data['price'] = np.array(prices)

        #comment the below lines if you don't want healthy/unhealthy prices
        healthy = food_data.loc[food_data['healthy'] == 'yes', 'price'].sum()
        unhealthy = food_data.loc[food_data['healthy'] == 'no', 'price'].sum()

        print(food_data)
        print()
        print("Healthy: $" + str(healthy))
        print("Unhealthy: $" + str(unhealthy))
        #print("Ratio: " + str(healthy/(healthy+unhealthy))[:4])
        print("Amount Donated: $" + str(healthy/10)[:4])
        print()
