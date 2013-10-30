#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from Tkinter import *
from tkFileDialog import askopenfilename

def open_file_and_close_root(): 
    root.destroy()

def assign_plotNum(*args):
    global plotNum
    plotNum = plotEntryNum.get()

def ask_file_name():
    global filename
    Tk().withdraw()
    filename = askopenfilename()

def read_from_file():
    global dataList
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

def plot_and_show():
    dataNum = len(dataList[0])
    x = np.arange(dataNum)
    for idx in range(plotNum):
        subplotPara = int( str(subplotList[plotNum]) + str(idx+1) )
        plt.subplot(subplotPara)
        plt.plot(x, dataList[idx], "r-")
    plt.show()

if __name__ == '__main__':
    
    filename = None
    plotNum = None
    
    dataList = list()
    subplotList = [0,11,21,22,22]
    
    root = Tk()
    topFrame = Frame(root)
    topFrame.pack()
    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)

    plotEntryNum = IntVar(value=None)
    plotEntryNum.trace('w', assign_plotNum)
    plotNum_label = Label(topFrame, text="Plot Number")
    plotNum_entry = Entry(topFrame, width="7", textvariable=plotEntryNum)
    plotNum_label.pack(side=LEFT)
    plotNum_entry.pack(side=LEFT)

    file_label = Label(bottomFrame, text="Data File")
    file_button = Button (bottomFrame, text="Open File", command=open_file_and_close_root)
    file_label.pack(side=LEFT)
    file_button.pack(side=LEFT)
    
    root.mainloop()
    ask_file_name()
    read_from_file()
    plot_and_show()
    





