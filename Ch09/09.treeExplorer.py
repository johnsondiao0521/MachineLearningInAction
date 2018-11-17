#encoding:utf-8

import _tkinter
from tkinter import *
from numpy import *

import matplotlib
matplotlib.use("TKAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def reDraw(tolS,tolN):
    reDraw.f.clf()
    reDraw.a=reDraw.f.add_subplot(111)
    #if chkBtnVar.get():


if __name__ == '__main__':

    root=Tk()
    myLabel=Label(root,text="hello world!!!")
    myLabel.grid()
    root.mainloop()
