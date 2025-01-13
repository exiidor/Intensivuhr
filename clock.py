import tkinter as tk
from time import *
import locale 

locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')
startDayAtHour = 8
endDayAtHour = 18

def update_time():
    current_time = strftime('%H:%M')
    weekday_name = strftime('%A')
    current_date = strftime('%d. %B %Y')  
    clock_label.config(text=current_time)
    weekday_label.config(text=weekday_name)
    date_label.config(text=current_date)
    root.after(1000, update_time)

def is_daytime():
    current_hour = int(strftime("%H"))
    if( startDayAtHour <= current_hour < endDayAtHour):
        return True
    else:
        return False

def color_background():
    if (is_daytime()):
        return "white"
    else:
        return "black"

def color_chars():
    if(is_daytime()):
        return "black"
    else:
        return "white"

def update_colors():
    bg_color = color_background()
    char_color = color_chars()
    root.config(bg=bg_color)
    frame.config(bg=bg_color)
    clock_label.config(fg=char_color, bg=bg_color)
    date_label.config(fg=char_color, bg=bg_color)
    weekday_label.config(fg=char_color, bg=bg_color)
    root.after(1000, update_colors) 

root = tk.Tk()

root.config(cursor="none")
root.title("Digital Clock")
root["bg"] = color_background()

frame = tk.Frame(root, bg=color_background())
frame.pack(expand=True)  


clock_label = tk.Label(
    frame, font=('Helvetica', 3*100), fg=color_chars(), bg=color_background(), anchor='center'
)
clock_label.pack()

date_label = tk.Label(
    frame, font=('Helvetica', 4*24), fg=color_chars(), bg=color_background(), anchor='center'
)
date_label.pack()

weekday_label = tk.Label(
    frame, font=('Helvetica', 4*24), fg=color_chars(), bg=color_background(), anchor='center'
)
weekday_label.pack()

update_time()

update_colors()

root.attributes('-fullscreen', True)

#root.overrideredirect(True), not working on RPZERO

root.mainloop()
