from tkinter import *
import time
import random
for i in range(40):
    root = Tk()
    root.title("Я списал!")
    def center_window():        
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()       
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        root.geometry('%dx%d+%d+%d' % (random.randint(100,500), random.randint(100,500), x, y))    
    center_window()  
    l=Label(root, text="Я списал у Колонистова")
   
    time.sleep(0.1)
    root.destroy()
    
