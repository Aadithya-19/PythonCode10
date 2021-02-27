import numpy as np
import csv
import plotly.express as ps
import pandas as spb

def plot_graph(path):

    with open(path) as f:
        df = csv.DictReader(f)
        graph = ps.scatter(df, x = "Size of TV", y = "\tAverage time spent watching TV in a week (hours)")
        graph.show()

def get_datasource(datapath):
    icecream = []
    temperature = []

    
    
    with open(datapath) as f:
        df = csv.DictReader(f)
        for a in df:
            temperature.append(float(a["Size of TV"]))
            icecream.append(float(a["\tAverage time spent watching TV in a week (hours)"]))
    return {
        "x":temperature,
        "y":icecream
    }


def corr(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print(correlation)

def main():
    plot_graph("./tempvsicevscold.csv")
    corr(get_datasource("./tempvsicevscold.csv"))


if __name__ == '__main__':
    main()
