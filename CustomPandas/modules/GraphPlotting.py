import pandas as pd
def graph_plotting_file_csv_data():
    print("\033[0;31mThe Graph of the this file data")
    h = str(input('\033[0;32mEnter File name with .csv extension to plot a graph of data of this file :'))
    df = pd.read_csv(h)
    df.plot()
    plt.show()


def graph_plotting_file_json_data(h):
    h = str(input('\033[0;34mEnter the name of the File with .json extension to plot its graph:'))
    df = pd.read_json(h)
    df.plot()
    plt.show()


def file_column_graph(h):
    h = str(input('\033[0;34mEnter the name of the File with .json extension to plot its graph:'))
    df = pd.read_json(h)
    f = str(input('\033[0;31mEnter the name of  the cloumn for x axis'))
    g = str(input('\033[0;31mEnter the name of the cloumn for y axis :'))
    df.plot(x=f, y=g)
    plt.show()


def file_column_graph_scatter(df):
    h = str(input('\033[0;34mEnter the name of the File with .json extension to plot its graph:'))
    df = pd.read_json(h)
    f = str(input('\033[0;31mEnter the name of  the cloumn for x axis'))
    g = str(input('\033[0;31mEnter the name of the cloumn for y axis :'))
    df.plot(kind='scatter', x=f, y=g)
    plt.show()


def file_column_histogram(df):
    h = str(input('\033[0;34mEnter the name of the File with .json extension to plot its graph:'))
    df = pd.read_json(h)
    f = str(input('\033[0;31mEnter the name of  the cloumn for x axis'))
    g = str(input('\033[0;31mEnter the name of the cloumn for y axis :'))
    df.plot(kind='hist', x=f, y=g)
    plt.show()


def file_column_pie_chart(df):
    h = str(input('\033[0;34mEnter the name of the File with .json extension to plot its graph:'))
    df = pd.read_json(h)
    f = str(input('\033[0;31mEnter the name of  the cloumn for x axis'))
    g = str(input('\033[0;31mEnter the name of the cloumn for y axis :'))
    df.plot(kind='hist', x=f, y=g)
    plt.show()

