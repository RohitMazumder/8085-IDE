import tkinter 
import os     
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class IDE8085: 
  
    __root = Tk() 
  
    # default window width and height 
    __root.grid()
    __root.title("Untitled - 8085") 
    frame=Frame(__root)
    Frame1 = Frame(__root, bg='#505050')
    Frame1.grid(row = 1, column = 0, rowspan = 3, columnspan = 4, sticky = W+E+N+S)
    vscrollbar = Scrollbar(Frame1, orient=VERTICAL)
    vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
    #canvas = Canvas(Frame1, bd=0, highlightthickness=0, bg='#505050',
                    #yscrollcommand=vscrollbar.set)
    canvas = Canvas(Frame1, bd=0, highlightthickness=0, bg='#505050',
                    yscrollcommand=vscrollbar.set)
    canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
    __thisTextArea = Text(canvas)
    __thisTextArea.pack(fill=BOTH)
    __thisTextArea.configure(background='#505050', fg="white")
    __thisTextArea.grid(sticky = N + E + S + W) 
    __thisTextArea.configure(background='#505050', fg="white")
    #vscrollbar.config(command=canvas.yview)
    Frame2 = Frame(__root, bg="blue")
    Frame2.grid(row = 4, column = 0, rowspan = 3, columnspan = 4, sticky = W+E+N+S)
    vscrollbar = Scrollbar(Frame2, orient=VERTICAL)
    vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
    canvas2 = Canvas(Frame2, bd=0, highlightthickness=0, bg="#ffffff",
                    yscrollcommand=vscrollbar.set)
    canvas2.pack(side=LEFT, fill=BOTH, expand=TRUE)
    vscrollbar.config(command=canvas.yview)
    
    Frame3 = Frame(__root, bg="black")
    Frame3.grid(row = 0, column = 4, rowspan = 6, columnspan = 3, sticky = W+E+N+S)
    __file = None
    def __init__(self, **kwargs):
        
        
        for r in range(6):
            self.__root.rowconfigure(r, weight=1) 
        self.__root.columnconfigure(0, weight=1)
        Button(self.__root, text="compile".format(0), command=self.__click).grid(row=6,column=0,sticky=E+W)
        self.__root.columnconfigure(1, weight=1)
        Button(self.__root, text="run".format(1)).grid(row=6,column=1,sticky=E+W)
        for c in range(4):
            self.__root.columnconfigure(c+2, weight=1)
            Button(self.__root, text="Button {0}".format(c+2)).grid(row=6,column=c+2,sticky=E+W)
    def __click(self): 
            file = open('temp2.txt',"w") 
            file.write(self.__thisTextArea.get(1.0,END)) 
            file.close()
    def run(self): # Run main application 
        self.__root.mainloop() 
  
IDE8085 = IDE8085() 
IDE8085.run() 