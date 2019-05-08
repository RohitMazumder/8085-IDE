import tkinter as tk
import os     
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from main import run

class IDE8085: 
  
    __root = Tk() 
    __root.grid()
    __root.title("8085_IDE")
    Image0 = tk.PhotoImage(file="tb.gif")
    Image00 = tk.PhotoImage(file="1.gif") 
    frame=Frame(__root)
    Frame0 = Frame(__root, bg="grey")
    Frame0.grid(row = 0, column = 0, rowspan = 1, columnspan = 14, sticky = W+E+N+S)
    canvas0 = Canvas(Frame0, bd=0, highlightthickness=0)
    canvas0.pack(side=TOP, fill=X)
    w1 = tk.Label(canvas0, image=Image0).pack(side=LEFT, fill=BOTH, expand=TRUE)
    Frame1 = Frame(__root, bg='#FEF79B')
    Frame1.grid(row = 1, column = 0, rowspan = 10, columnspan = 10, sticky = W+E+N+S)
    vscrollbar = Scrollbar(Frame1, orient=VERTICAL)
    vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
    xscrollbar = Scrollbar(Frame1, orient=HORIZONTAL)
    xscrollbar.pack(side=BOTTOM, fill=X)
    canvas = Canvas(Frame1, bd=0, highlightthickness=0, bg='#FEF79B',
                    yscrollcommand=vscrollbar.set)
    canvas.configure(xscrollcommand=xscrollbar.set)
    canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
    canvas.grid_columnconfigure(0, weight=1)
    __thisTextArea = Text(canvas,font=("calibri",12))
    __thisTextArea.pack(expand=True, fill='both')
    __thisTextArea.configure(background='#D8BFD8', fg="black")
    __thisTextArea.grid(sticky = N + E + S + W) 
    Frame00 = Frame(__root, bg="grey")
    Frame00.grid(row = 11, column = 0, rowspan = 1, columnspan = 10, sticky = W+E+N+S)
    canvas00 = Canvas(Frame00, bd=0, highlightthickness=0)
    canvas00.pack(side=TOP, fill=X)
    w2 = tk.Label(canvas00, image=Image00).pack(side=LEFT, fill=Y, expand=TRUE)
    Frame2 = Frame(__root)
    Frame2.grid(row = 12, column = 0, rowspan = 9, columnspan = 10, sticky = W+E+N+S)
    vscrollbar = Scrollbar(Frame2, orient=VERTICAL)
    vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
    canvas2 = Canvas(Frame2, bd=0, highlightthickness=0, bg='#FEF79B',
                    yscrollcommand=vscrollbar.set)
    canvas2.pack(side=LEFT, fill=BOTH, expand=TRUE)
    canvas2.grid_columnconfigure(0, weight=1)
    __thisTextArea2 = Text(canvas2,font=("times new roman",12))
    __thisTextArea2.pack(expand=True, fill='both')
    __thisTextArea2.configure(background='#D8BFD8', fg="black")
    __thisTextArea2.grid(sticky = N + E + S + W) 
    vscrollbar.config(command=canvas.yview)
    
    Frame3 = Frame(__root, bg='#191970')
    Frame3.grid(row = 1, column = 10, rowspan = 19, columnspan = 4, sticky = W+E+N+S)
    __file = None
    
    Image = tk.PhotoImage(file="cmp.gif") 
    Image2 = tk.PhotoImage(file="run.gif") 
    def __init__(self, **kwargs):
        
        self.widgets()
        for r in range(20):
            self.__root.rowconfigure(r, weight=1)
        for r in range(20):
            self.__root.columnconfigure(r, weight=1)
        Button(self.__root, image=self.Image,compound="top", command=self.__click).grid(row=0,column=0,sticky=N+W) 
        Button(self.__root, image=self.Image2,compound="top", command=self.__run).grid(row=0,column=0,sticky=N) 
    def __click(self):
        path="temp.txt"
        file = open(path,"w+") 
        file.write(self.__thisTextArea.get(1.0,END)) 
        file.close()
        run(path)
        os.remove(path)
    def __run(self):
        path="out.txt"
        self.__thisTextArea2.delete(1.0,END) 
        file = open(path,"r") 
        self.__thisTextArea2.insert(1.0,file.read()) 
        file.close() 
        os.remove("out.txt")
    def widgets(self):


        menubar = Menu(self.__root)
        filemenu=Menu(menubar)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label = "New                Ctrl+N", command = "")
        filemenu.add_command(label = "Open", command = "" )
        filemenu.add_separator()
        filemenu.add_command(label = "Save               Ctrl+S", command =self.__save)
        filemenu.add_command(label = "Duplicate", command = "" )
        filemenu.add_command(label = "Rename", command = "")
        editmenu=Menu(menubar)
        menubar.add_cascade(label="Edit", menu=editmenu)
        
        editmenu.add_command(label="Cut              Ctrl+X", command=self.__cut )              
        editmenu.add_command(label="Copy           Ctrl+C" , command=self.__copy )          
        editmenu.add_command(label="Paste            Ctrl+V", command=self.__paste)   
        menubar.add_cascade(label="Help")

        self.__root.config(menu=menubar)
    def __save(self):
        if self.__file == None: 
            # Save as new file 
            self.__file = asksaveasfilename(initialfile='Untitled.txt', 
                                            defaultextension=".txt", 
                                            filetypes=[("All Files","*.*"), 
                                                ("Text Documents","*.txt")]) 
  
            if self.__file == "": 
                self.__file = None
            else: 
                  
                # Try to save the file 
                file = open(self.__file,"w") 
                file.write(self.__thisTextArea.get(1.0,END)) 
                file.close() 
                  
                # Change the window title 
                self.__root.title(os.path.basename(self.__file) + " - 8085_IDE") 
                  
              
    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")
    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")
    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")
    
    def run(self): # Run main application 
        self.__root.mainloop() 
  
IDE8085 = IDE8085() 
IDE8085.run() 
