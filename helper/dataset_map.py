import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy as sci
import pandas as pd
import difflib

def get_index(words):
    dataset = pd.read_csv("./data/food_data.csv")
    df = pd.DataFrame(dataset)
    names = df['Shrt_Desc']
    names = np.array(names)

    best_answer_index = []
    for word in words:
        answer = difflib.get_close_matches(word.upper(),names,10,.2)
        best_answer_index.append(int((np.where(names==answer[0])[0])))

    return best_answer_index
