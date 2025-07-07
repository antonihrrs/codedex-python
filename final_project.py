import time
import tkinter
from tkinter import messagebox

def countdown(t):
    while t >= 0 :
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        timer_label.config(text=timer)
        window.update()
        time.sleep(1)
        t -= 1
    
    timer_label.config(text="Time is up :)")


def get_time(user_input):
    while True:
        try: 
            t = int(user_input)
            return t
            
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number")
            return None

def click_button():
    user_input = user_box.get()
    t = get_time(user_input)
    if t is not None:
        countdown(t)

window = tkinter.Tk()
window.title("Timer")
window.geometry("400x175")


instruction_text = tkinter.Label(window, text="Enter the time in seconds : ")
instruction_text.pack()

user_box = tkinter.Entry(window)
user_box.pack()

start_button = tkinter.Button(window, text="Start timer", command=click_button)
start_button.pack()

timer_label = tkinter.Label(window, text="")
timer_label.pack()

window.mainloop()