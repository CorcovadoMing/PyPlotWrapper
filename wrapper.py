import matplotlib.pyplot as plt
import numpy as np

dataList = list()

def read_from_file(filename, plotNum):
    for x in range(plotNum):
        dataList.append(list())
            
    file = open(filename, 'r')
    while True:
        for x in range(plotNum):
            data = file.readline()
            if data == '': 
                file.close()
                return
            else:
                dataList[x].append(float(data))

def plot_and_show(plotNum):
    subplotList = [0,11,21,22,22]
    dataNum = len(dataList[0])
    x = np.arange(dataNum)
    for idx in range(plotNum):
        subplotPara = int( str(subplotList[plotNum]) + str(idx+1) )
        plt.subplot(subplotPara)
        plt.plot(x, dataList[idx], "r-")
    plt.show()
    





