from tkinter import *
from tkinter.ttk import *

from time import strftime

interface= Tk()
p1= PhotoImage(file= 'clock3-6.png')
interface.title("Digital clock")
interface.iconphoto(False, p1)

def time():
    string = strftime('%I:%M:%S:%p')
    label.config(text=string)
    label.after(1000,time)

label= Label(interface, font=("Minion Pro",80), background="black", foreground="cyan")
label.pack(anchor='center')
time()

mainloop()



# Description
# Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications. 
# ttk is a module that is used to style the tkinter widgets. Just like CSS is used to style an HTML element, we use tkinter. ttk to style tkinter widgets.
# The strftime() function is used to convert date and time objects to their string representation.
# Tk is a free and open-source, cross-platform widget toolkit that provides a library of basic elements of GUI widgets for building a graphical user interface (GUI) in many programming languages.
# Tkinter Label is a widget that is used to implement display boxes where you can place text or images.
# The pack() fill option is used to make a widget fill the entire frame.
# mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed.






