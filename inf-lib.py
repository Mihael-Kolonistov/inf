from tkinter import *
import time
import random
for i in range(40):
    root = Tk()
    root.title("Я списал!")  
    l=Label(root, text="Я списал у Колонистова", font=("Arial", 50), background="red")
    l.grid()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()       
    x = random.randint(0, 1000)
    y = random.randint(0, 1000)
    root.geometry('%dx%d+%d+%d' % (760,80, x, y))     
    root.mainloop()
    
