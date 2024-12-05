import tkinter as tk
from time import *
import locale

#Delet localtime

locale.setlocale(locale.LC_TIME, 'deu_deu') 

def update_time():
    current_time = strftime('%H:%M')
    weekday_name = strftime('%A')
    current_date = strftime('%d. %B %Y')  
    clock_label.config(text=current_time)
    weekday_label.config(text=weekday_name)
    date_label.config(text=current_date)
    root.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")
root["bg"] = "black"

frame = tk.Frame(root, bg='black')
frame.pack(expand=True)  


clock_label = tk.Label(
    frame, font=('Helvetica', 3*100), fg='white', bg='black', anchor='center'
)
clock_label.pack()

date_label = tk.Label(
    frame, font=('Helvetica', 4*24), fg='white', bg='black', anchor='center'
)
date_label.pack()

weekday_label = tk.Label(
    frame, font=('Helvetica', 4*24), fg='white', bg='black', anchor='center'
)
weekday_label.pack()

update_time()

#fullscreen is broken on rp nano
root.attributes('-fullscreen', True)

root.overrideredirect(True)

root.mainloop()
