import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy as sci
import pandas as pd
import difflib
import csv

path_to_file = '/Users/aditgupta/Google_Drive/ABBREV.csv'

dataset = pd.read_csv(path_to_file)
df = pd.DataFrame(dataset)
names = df['Shrt_Desc']
names = np.array(names)

words = ['granola', 'af trail mix fn', 'lunate', 'crunch', 'grapes', 'paper bag fee']
best_answer_index = []
for word in words:
    answer = difflib.get_close_matches(word.upper(),names,10,.4)
    best_answer_index.append(int((np.where(names==answer[0])[0])))


#read food data
all_parsed_food = pd.read_csv(path_to_file,delimiter=",", header = None)

#index 48 is grams in one serving
#index 3 is the calories in one serving

#change the healthy_value based on what you think the cal/g for healthiness is
healthy_value = 55

all_food = all_parsed_food.drop([0])
#convert index 3 and 48 for int
all_food = all_food.astype({3: float, 48: float})
#cal/g is the amount of calories per gram of food
all_food["cal/g"] = all_food[3]/all_food[48]
#determines if a food is healthy or not
all_food["healthy"] = ['yes' if x <= healthy_value else 'no' for x in all_food["cal/g"]]

healthiness_food = all_food.drop(columns=[0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52])
all_desired_details = healthiness_food.iloc[best_answer_index,:]

#all_desired_details includes all important infromation desired from food
all_desired_details
