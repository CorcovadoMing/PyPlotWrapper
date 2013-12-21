import matplotlib.pyplot as plt
import numpy as np

def read_from_file(filename, plotNum, dataList):
    file = open(filename, 'r')
    while True:
        for x in range(plotNum):
            data = file.readline()
            if data == '': 
                file.close()
                return
            else:
                dataList[x].append(float(data))

def plot_subarea(plotNum, subplotArea, dataList):
    subplotList = [0,11,21,22,22]
    dataNum = len(dataList[0])
    x = np.arange(dataNum)
    subplotParameter = int( str(subplotList[plotNum]) + str(subplotArea+1) )
    plt.subplot(subplotParameter)
    plt.plot(x, dataList[subplotArea], "r-")

def plot_and_show(plotNum, dataList):
    for subplotArea in range(plotNum):
        plot_subarea(plotNum, subplotArea, dataList)
    plt.show()
    





