from tkinter import *
import time
import random
for i in range(40):
    root = Tk()
    root.title("Я списал!")  
    l=Label(root, text="Я списал у Колонистова")
    l.grid()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()       
    x = random.randint(0, 1000)
    y = random.randint(0, 1000)
    root.geometry('%dx%d+%d+%d' % (random.randint(100,500), random.randint(100,500), x, y))  
    time.sleep(1)
    root.destroy()
    
