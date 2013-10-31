import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

dataList = list()

def construct_dataList(plotNum):
    for x in range(plotNum):
        dataList.append(list())

def read_from_file(filename, plotNum):
    construct_dataList(plotNum)
    file = open(filename, 'r')
    while True:
        for x in range(plotNum):
            data = file.readline()
            if data == '': 
                file.close()
                return
            else:
                dataList[x].append(float(data))

def plot_subarea(plotNum, subplotArea, fig):
    subplotList = [0,11,21,22,22]
    dataNum = len(dataList[0])
    x = np.arange(dataNum)
    z = np.zeros(dataNum)
    subplotParameter = int( str(subplotList[plotNum]) + str(subplotArea+1) )
    #plt.subplot(subplotParameter)
    ax = fig.add_subplot(subplotParameter, projection='3d')
    ax.plot(x, z, dataList[subplotArea])

def plot_and_show(plotNum):
    fig = plt.figure()
    fig.suptitle('3D Plot')
    for subplotArea in range(plotNum):
        plot_subarea(plotNum, subplotArea, fig)
    plt.show()
    





