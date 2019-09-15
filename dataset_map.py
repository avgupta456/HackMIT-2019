import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy as sci
import pandas as pd
import difflib

def get_index(words):
    dataset = pd.read_csv("ABBREV.csv")
    df = pd.DataFrame(dataset)
    names = df['Shrt_Desc']
    names = np.array(names)

    best_answer_index = []
    for word in words:
        answer = difflib.get_close_matches(word.upper(),names,10,.2)
        best_answer_index.append(int((np.where(names==answer[0])[0])))

        '''
        best = 0
        value = 0
        for i in range(len(names)):
            temp = difflib.SequenceMatcher(None, word.upper(), names[i]).ratio()
            if(temp>value): [best, value] = [i, temp]

        best_answer_index.append(best)
        '''

    return best_answer_index
