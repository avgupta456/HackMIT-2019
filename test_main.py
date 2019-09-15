import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np
import scipy as sci
import pandas as pd

from dataset_map import get_index
from food_predict import get_food_info
from food_data import healthyness

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
        parsed_data = get_food_info(foods_index)
        health = healthyness(parsed_data,prices)
        print()
