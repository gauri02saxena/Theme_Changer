#Importing Tkinter in the environment
from tkinter import *

#Creating a window
window=Tk()
window.title("Theme Changer")  #Adding titlte to the window
window.geometry("600x800")      #Setting geometry of the window
window.config(bg="white")       #Setting the background color of the window


#Adding light and dark mode images 
light=PhotoImage(file="C:\\Users\\GAURI\\Downloads\\light.png")
dark=PhotoImage(file="C:\\Users\\GAURI\\Downloads\\dark.png")

switch_value=True

#defining a function to toggle between light and dark theme 
def toggle():
    
    global switch_value
    if switch_value==True:
        switch.config(image=dark,bg="#26242f",activebackground="#26242f")#Changes the window to dark theme by replacing the white background and light.png
        window.config(bg="#26242f")
        switch_value=False

    else:
        switch.config(image=light, bg="white",activebackground="white") #Changes the window to light theme by replacing the dark background and dark.png 
        window.config(bg="white")
        switch_value=True
        
        
#Creating a button to switch themes

switch= Button(window, image=light, bd=0, bg="white",activebackground="white",command=toggle)
switch.pack(padx=50, pady=150)


window.mainloop()
