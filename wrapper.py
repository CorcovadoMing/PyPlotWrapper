import matplotlib.pyplot as plt
import numpy as np
from Tkinter import *
from tkFileDialog import askopenfilename


filename = None
plotNum = None

def close_window(): 
    window.destroy()

def assign_plotNum(*args):
    global plotNum
    plotNum = plotEntryNum.get()

window = Tk()
topFrame = Frame(window)
topFrame.pack()

bottomFrame = Frame(window)
bottomFrame.pack(side=BOTTOM)
plotEntryNum = IntVar(value=None)
plotEntryNum.trace('w', assign_plotNum)
plotNum_label = Label(topFrame, text="Plot Number")
plotNum_entry = Entry(topFrame, width="7", textvariable=plotEntryNum)
plotNum_label.pack(side=LEFT)
plotNum_entry.pack(side=LEFT)

file_label = Label(bottomFrame, text="Data File")
file_button = Button (bottomFrame, text="Open File" , command = close_window)
file_label.pack(side=LEFT)
file_button.pack(side=LEFT)
window.mainloop()

def askFileName():
    global filename
    Tk().withdraw()
    filename = askopenfilename()


try:
    askFileName()
except :
    pass

dataList = list()
subplotList = [0,11,21,22,22]

for x in range(plotNum):
    dataList.append(list())

def read_from_file():
    global dataList    
    file = open(filename, 'r')
    while True:
        for x in range(plotNum):
            data = file.readline()
            if data == '': 
                file.close()
                return
            else:
                dataList[x].append(float(data))

read_from_file()

dataNum = len(dataList[0])
x = np.arange(dataNum)
for idx in range(plotNum):
    subplotPara = int( str(subplotList[plotNum]) + str(idx+1) )
    plt.subplot(subplotPara)
    plt.plot(x, dataList[idx], "r-")
plt.show()

