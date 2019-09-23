import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy as sci
import pandas as pd
import csv

def get_food_info(foods):
    #read food data
    path_to_file = './data/food_data.csv'
    all_parsed_food = pd.read_csv(path_to_file, delimiter=",", header = None)

    #index 48 is grams in one serving
    #index 3 is the calories in one serving

    all_food = all_parsed_food.drop([0])

    #convert index 3 and 48 for int
    all_food = all_food.astype({2: float, 3: float, 4: float, 5: float, 6: float, 7: float, 8: float, 9: float, 15: float})
    all_food = all_food.replace([np.inf, -np.inf], np.nan)
    all_food = all_food.fillna(0)

    #cal/g is the amount of calories per gram of food
    all_food["weight"] = all_food[2]+all_food[4]+all_food[5]+all_food[6]+all_food[7]+all_food[8]+all_food[9]

    all_food["cal/g"] = all_food[3]/all_food["weight"]*100

    all_food["fat/g"] = all_food[5]/all_food["weight"]*100
    all_food["fat/g"] = [1 if x > 8 else 0 for x in all_food["fat/g"]]

    all_food["sugar/g"] = all_food[9]/all_food["weight"]*100
    all_food["sugar/g"] = [1 if x > 40 else 0 for x in all_food["sugar/g"]]

    all_food["salt/g"] = all_food[15]/all_food["weight"]/10 #mg not g
    all_food["salt/g"] = [1 if x > 1 else 0 for x in all_food["salt/g"]]

    all_food["total"] = all_food["fat/g"] + all_food["sugar/g"] + all_food["salt/g"]
    all_food["healthy"] = ["yes" if x==0 else "no" for x in all_food["total"]]

    healthiness_food = all_food.drop(columns=[0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52])
    all_desired_details = healthiness_food.iloc[foods,:]

    #all_desired_details includes all important infromation desired from food
    return all_desired_details
