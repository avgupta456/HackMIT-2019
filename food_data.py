import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy as sci
import pandas as pd

def healthyness(data,prices):
    health_map = np.array(data[0]['healthy'])
    bad_prices = []
    good_prices = []
    for i in range(len(health_map)):
        if health_map[i] == False:
            bad_prices.append(prices[i])
        else:
            good_prices.append(prices[i])
    print(sum(bad_prices))
    print(sum(good_prices))
