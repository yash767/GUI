#The GUI
#DATE : 20/6
#AUTHOR : Yash Kakatkar

from tkinter import *
import xml.etree.ElementTree as ET
tree=ET.parse('C:\\Users\\Yash\\Downloads\\trial.xml.txt')
root=tree.getroot()

    

def radiobutton():
    top = Toplevel()
    
    
        
            
                
    """def hello():
        print("%d" % (var.get()))
        print("Check var %d "% (CheckVar1.get()))"""
   
    var=IntVar()
    CheckVar1=IntVar()
    i=0
    for child in root:
        for j in range (0,(len(child))):
            if(root[i][j].tag=="board"):
                radio=Radiobutton(top, text=((root[i][j].text),":"),variable=var,value=(i+1))
                
                radio.pack( anchor = W)
            else:
                
                check = Checkbutton(top, text = root[i][j].text, onvalue = j, offvalue = 0)
                check.config()
                check.pack()
                
                
            
        i=i+1
    top.mainloop()


window=Tk()

# Navigation Bar
menubar=Menu(window)

# TEST pulldown menu

testmenu=Menu(menubar, tearoff=0)
testmenu.add_command(label="Run")
testmenu.add_separator()

testmenu.add_command(label="Log")
menubar.add_cascade(label="Test", menu=testmenu)

# SETUP button

menubar.add_command(label="Setup",command=radiobutton)

window.config(menu=menubar)
window.mainloop()

