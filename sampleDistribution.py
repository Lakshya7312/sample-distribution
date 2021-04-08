import csv
import pandas as pd
import statistics
import random
import plotly.figure_factory as ff

dataFrame = pd.read_csv("medium_data.csv")
data = dataFrame["claps"].tolist()

population_mean = statistics.mean(data)
print(population_mean)

def samples(rand):
    dataSet = []

    for i in range(0, rand):
        randomIndex = random.randint(0, len(data) - 1)
        value = data[randomIndex]
        dataSet.append(value)

    mean = statistics.mean(dataSet)
    return(mean)
    print(mean)

def setup():
    meanList = []

    for i in range(0, 100):
        setOfMeans = samples(30)
        meanList.append(setOfMeans)

    plot_graph(meanList)

def plot_graph(dataList):
    dataFrame1 = dataList
    graph = ff.create_distplot([dataFrame1], ["Claps"], show_hist=False)
    graph.show()


setup()