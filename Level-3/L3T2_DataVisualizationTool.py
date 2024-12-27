# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 09:45:19 2024

@author: rawqa
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def plot_data(data,plot_type,x_col=None,y_col=None):
    plt.figure(figsize=(10,6))
    if(plot_type=='scatter'):
        plt.scatter(data[x_col],data[y_col],color='red')
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f"Scatter: {x_col} Vs {y_col}")
    elif(plot_type=='bar'):
        data[x_col].value_counts().plot(kind='bar',color='green')
        plt.xlabel(x_col)
        plt.ylabel('Count')
        plt.title(f"BarPlot of {x_col}")
    elif(plot_type=='histogram'):
        plt.hist(data[x_col],bins=30,color='violet')
        plt.xlabel(x_col)
        plt.ylabel('Frequency')
        plt.title(f"Histogram of {x_col}")
    elif(plot_type=='box'):
        plt.boxplot(data[x_col])
        plt.ylabel(x_col)
        plt.title(f"BoxPlot of {x_col}")
    plt.tight_layout()
    plt.show()
data=pd.DataFrame({
    'age': np.random.normal(30, 10, 100),
    'salary': np.random.normal(50000, 10000, 100),
    'department': np.random.choice(['HR', 'IT', 'Sales'], 100)   
    })
plot_data(data,'scatter','age','salary')
plot_data(data,'bar',x_col='department')
plot_data(data, 'histogram', x_col='age')
plot_data(data,'box',x_col='salary')
        