import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy as sci
import pandas as pd
import difflib

def get_index():
    dataset = pd.read_csv("ABBREV.csv")
    df = pd.DataFrame(dataset)
    names = df['Shrt_Desc']
    names = np.array(names)
    
    words = ['orange','orange juice']
    best_answer_index = []
    for word in words:
        answer = difflib.get_close_matches(word.upper(),names,10,.4)
        print(answer)
        best_answer_index.append(int((np.where(names==answer[0])[0])))

    print(best_answer_index)
