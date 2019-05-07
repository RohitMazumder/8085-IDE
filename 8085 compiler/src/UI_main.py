import tkinter 
import os     
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from main import run
import subprocess

class IDE8085: 
  
    __root = Tk() 
    __root.grid()
    __root.title("Untitled - 8085") 
    frame=Frame(__root)
    Frame1 = Frame(__root, bg='#505050')
    Frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 4, sticky = W+E+N+S)
    vscrollbar = Scrollbar(Frame1, orient=VERTICAL)
    vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
    xscrollbar = Scrollbar(Frame1, orient=HORIZONTAL)
    xscrollbar.pack(side=BOTTOM, fill=X)
    canvas = Canvas(Frame1, bd=0, highlightthickness=0, bg='#505050',
                    yscrollcommand=vscrollbar.set)
    canvas.configure(xscrollcommand=xscrollbar.set)
    canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
    canvas.grid_columnconfigure(0, weight=1)
    __thisTextArea = Text(canvas)
    __thisTextArea.pack(expand=True, fill='both')
    __thisTextArea.configure(background='#505050', fg="white")
    __thisTextArea.grid(sticky = N + E + S + W) 
    __thisTextArea.configure(background='#505050', fg="white")

    Frame2 = Frame(__root, bg="blue")
    Frame2.grid(row = 4, column = 0, rowspan = 3, columnspan = 4, sticky = W+E+N+S)
    vscrollbar = Scrollbar(Frame2, orient=VERTICAL)
    vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
    canvas2 = Canvas(Frame2, bd=0, highlightthickness=0, bg="#505050",
                    yscrollcommand=vscrollbar.set)
    canvas2.pack(side=LEFT, fill=BOTH, expand=TRUE)
    canvas.grid_columnconfigure(0, weight=1)
    __thisTextArea2 = Text(canvas2)
    __thisTextArea2.pack(expand=True, fill='both')
    __thisTextArea2.configure(background='#505050', fg="white")
    __thisTextArea2.grid(sticky = N + E + S + W) 
    __thisTextArea2.configure(background='#505050', fg="white")
    vscrollbar.config(command=canvas.yview)
    
    Frame3 = Frame(__root, bg="black")
    Frame3.grid(row = 0, column = 4, rowspan = 6, columnspan = 3, sticky = W+E+N+S)
    __file = None
    def __init__(self, **kwargs):
        
        self.widgets()
        for r in range(6):
            self.__root.rowconfigure(r, weight=1) 
        self.__root.columnconfigure(0, weight=1)
        photo=tk.PhotoImage(file="img.gif")
        Button(self.__root, image=photo, text="compile".format(0), compound="top", command=self.__click).grid(row=6,column=0,sticky=E+W)
        self.__root.columnconfigure(1, weight=1)
        Button(self.__root, text="run".format(1), command=self.__run).grid(row=6,column=1,sticky=E+W)
        for c in range(4):
            self.__root.columnconfigure(c+2, weight=1)
            Button(self.__root, text="Button {0}".format(c+2)).grid(row=6,column=c+2,sticky=E+W)
    def __click(self):
            path="temp.txt"
            file = open(path,"w+") 
            file.write(self.__thisTextArea.get(1.0,END)) 
            file.close()
            run(path)
            os.remove(path)
    def __run(self):
        command = ['ls', '-l']
        p = subprocess.Popen(command)
        text = p.stdout.read()
        retcode = p.wait()
    def widgets(self):


        menubar = Menu(self.__root)
        filemenu=Menu(menubar)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label = "New", command = "")
        filemenu.add_command(label = "Open", command = "" )
        filemenu.add_separator()
        filemenu.add_command(label = "Save", command =self.__save)
        filemenu.add_command(label = "Duplicate", command = "" )
        filemenu.add_command(label = "Rename", command = "")
        editmenu=Menu(menubar)
        menubar.add_cascade(label="Edit", menu=editmenu)
        
        editmenu.add_command(label="Cut", command=self.__cut )              
        editmenu.add_command(label="Copy", command=self.__copy )          
        editmenu.add_command(label="Paste", command=self.__paste)   
        menubar.add_cascade(label="Quit")

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
                self.__root.title(os.path.basename(self.__file) + " - 8085IDE") 
                  
              
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