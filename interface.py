#!/usr/bin/env python
from wrapper import *
from Tkinter import *
from tkFileDialog import askopenfilename

def open_file_and_close_root(): 
    root.destroy()

def assign_plotNum(*args):
    global plotNum
    try:
        plotNum = plotEntryNum.get()
    except:
        pass

def ask_file_name():
    global filename
    Tk().withdraw()
    filename = askopenfilename() 
 
if __name__ == '__main__':
    plotNum = None
    filename = None
    
    root = Tk()
    root.title("PyPlotWrapper")
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
    read_from_file(filename, plotNum)
    plot_and_show(plotNum)
    