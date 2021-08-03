from tkinter import *
import records
from tkinter import messagebox

root = Tk()
root.title("PDF Reader")
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
bgc = "#adb5bd"
root.configure(bg=bgc)

bgImg = PhotoImage(file='images.png')

logoLabel = Label(image=bgImg, bg=bgc, width=1000, height=170)
logoLabel.place(x=0, y=130)

# INSTRUCTIONS
instructions = Label(text="Select a PDF file on your computer to extract all its text", bg=bgc, font="Raleway")
instructions.place(x=300, y=325)


# top right x button
def close():
    closeBtn = Button(text="X", command=on_closing, bg="#efefd0", fg="black", height=2, width=5)
    closeBtn.place(x=1235, y=1)


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()


# opening pdf with the browse button
def file():
    records.content()
    return


# opening new pdf through menu
def secondFile():
    records.secondContent()
    return


# clear text
def clearText():
    records.clearTextBox()
    return


# search for pdf nd display menu
def openFile():
    browseText.set("Loading...")
    file()

    # Menu
    myMenu = Menu(root)
    root.config(menu=myMenu)

    # Drop Down
    fileMenu = Menu(myMenu, tearoff=False)
    myMenu.add_cascade(label="MENU", menu=fileMenu)
    fileMenu.add_command(label="Open", command=secondFile)
    fileMenu.add_command(label="Clear", command=clearText)
    # fileMenu.add_command(label="Page", command=select)
    fileMenu.add_separator()
    close()

    browseText.set("Browse")


# BROWSE BUTTON
browseText = StringVar()
browseBtn = Button(textvariable=browseText, command=openFile, font="Raleway", bg="#efefd0",
                   fg="black", height=2, width=15)
browseBtn.place(x=50, y=200)

browseText.set("Browse")
browseBtn.place(x=425, y=400)

# close button
close()
root.mainloop()
