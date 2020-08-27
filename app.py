"""Imports"""
import pandas as pd
import datetime
from tkinter import Tk, Label, Button, filedialog, messagebox
from PIL import Image, ImageTk

#Window
root = Tk()
root.title('File Converter')
root.geometry("600x450")
root.resizable(0, 0)

#Window Icon
p1 = Image.open('iconpy.png')
photoImg = ImageTk.PhotoImage(p1)
root.iconphoto(False, photoImg)

#Background Image
bg = Image.open('bg.png')
photoBg = ImageTk.PhotoImage(bg)
labelBg = Label(root, image= photoBg, bd=0, highlightthickness=0)
labelBg.pack()
new_label = Label(root, text="The Software will check the file format and convert it to the other format")
new_label.place()

#Open Dialogue
def choose_file():
    root.filename = filedialog.askopenfilename(initialdir= "Pictures", title= "Select a file", filetypes= (("csv files", "*.csv"), ("excel files", "*.xlsx"),("all files", "*.*"))) 
    if root.filename.split('.')[-1] == 'csv':
        excelconv(root.filename)
    elif root.filename.split('.')[-1] == 'xlsx':
        csvconv(root.filename)
    else:
        messagebox.Message(master=root, message= "Invalid File Format")

#Conversion Functions
def csvconv(the_file):
    df = pd.read_excel(the_file) 
    filename=datetime.datetime.now().strftime("csv result/%Y-%m-%d-%H-%M-%S-%f"+".csv")
    df.to_csv(filename,index=None) 

def excelconv(the_file):
    df = pd.read_csv(the_file)
    filename=datetime.datetime.now().strftime("excel result/%Y-%m-%d-%H-%M-%S-%f"+".xlsx")
    df.to_excel(filename,index=None)  
    


button1 = Button(root, text= "Choose File", command= choose_file)
button1.place(x= 256, y= 290, width= 94, height= 50)


root.mainloop()