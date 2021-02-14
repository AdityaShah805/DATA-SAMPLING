import plotly.figure_factory as ff
import statistics
import random
import pandas as pd 
import csv

df=pd.read_csv("newdata.csv")
data=df["average"].tolist()
population_mean=statistics.mean(data)
standard_deviation=statistics.stdev(data)
print("population_mean",population_mean)
print("standard_deviation",standard_deviation)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def show_fig(mean_list):        
    df=mean_list
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],["average"],show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,1000):
        setofmeans=random_set_of_mean(100)
        mean_list.append(setofmeans)
    show_fig(mean_list)
    mean=statistics.mean(mean_list)
    print("samplingmean",mean)

setup()

def std_dev():
    mean_list=[]
    for i in range(0,1000):
        setofmeans=random_set_of_mean(100)
        mean_list.append(setofmeans)
    show_fig(mean_list)
    stddev=statistics.stdev(mean_list)
    print("samplingstdev",stddev)

std_dev()