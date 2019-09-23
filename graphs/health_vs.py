import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy as sci
import pandas as pd

plt.style.use('ggplot')

x=(1,2)
y=(170.02,197.47)
plt.title("Distribution of Spending in January")
plt.bar(x,y,color='red')
plt.xticks([])
plt.ylabel("$ Amount spent on category")
plt.xlabel("Healthy Value                        Unhealthy Value")
plt.show()
