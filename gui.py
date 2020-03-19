#sudo apt-get install python3-tk

from tkinter import *
from tkinter import filedialog
from parser import *



def browseXML():

    window.filename =  filedialog.askopenfilename(initialdir = "/", title = "Select XML file")
    
    if(len(window.filename) < 40):
        txt.configure(text=window.filename, anchor = "w") 
    elif(len(window.filename) > 40):
        txt.configure(text=window.filename, anchor = "e")
    

    
def browseDTD():

    window.filename =  filedialog.askopenfilename(initialdir = "/", title = "Select DTD file")
    
    if(len(window.filename) < 40):
        txt2.configure(text=window.filename, anchor = "w") 
    elif(len(window.filename) > 40):
        txt2.configure(text=window.filename, anchor = "e")

def browseOutputDirectory():

    window.filename =  filedialog.askdirectory()
    
    if(len(window.filename) < 40):
        txt3.configure(text=window.filename, anchor = "w") 
    elif(len(window.filename) > 40):
        txt3.configure(text=window.filename, anchor = "e")

def splitFile():

    #try:
        split(txt['text'],txt2['text'],txt3['text'])
    #except:
        #print("Error in parser")


window = Tk()

window.resizable(False,False)

window.title("DBLP Splitter")

window.geometry('450x135')

lbl = Label(window, text="  XML file:")

lbl.grid(column=0, row=0)

txt = Label(window, text="", width = 30, bg = "white")

txt.grid(column=1, row=0)

btn = Button(window, text="Browse", command=browseXML)

btn.grid(column=2, row=0)



lbl2 = Label(window, text=" DTD file:")

lbl2.grid(column=0, row=1)

txt2 = Label(window, text="", width = 30, bg = "white")

txt2.grid(column=1, row=1)

btn2 = Button(window, text="Browse", command=browseDTD)

btn2.grid(column=2, row=1)



lbl3 = Label(window, text=" Output Directory:")

lbl3.grid(column=0, row=2)

txt3 = Label(window, text="", width = 30, bg = "white")

txt3.grid(column=1, row=2)

btn3 = Button(window, text="Browse", command=browseOutputDirectory)

btn3.grid(column=2, row=2)




btn4 = Button(window, text="Split", width = 10,command=splitFile)

btn4.grid(column=1, row=3)

window.mainloop()