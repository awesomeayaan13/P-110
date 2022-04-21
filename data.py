import plotly.figure_factory as ff
import random
import statistics
import pandas as pd
import plotly.graph_objects as go
import csv

df=pd.read_csv("medium_data.csv")
data=df["id"].tolist()
populationMean=statistics.mean(data)
populationSTDev=statistics.stdev(data)
print(populationMean)
print(populationSTDev)

def random_set_in_mean(counter):
    dataSet=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return mean

def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_means=random_set_in_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],["id"], show_hist=False)
    fig.show
