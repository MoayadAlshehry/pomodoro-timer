from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    global my_timer
    if my_timer is not None:
        window.after_cancel(my_timer)
    time_lb.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text,text="00:00")
    check_mark.config(text="")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    reps += 1

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        time_lb.config(text="Work" , fg=GREEN)
        timer(0.10 *60)
    elif reps == 2 or reps == 4 or reps == 6:
        time_lb.config(text="Break", fg=PINK)
        timer(0.10 * 60)
    else:
        time_lb.config(text="Long Break",fg=RED)
        timer(1 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def timer(t):
    global my_timer
    min = math.floor(t / 60)
    sec = t % 60
    mark = ""
    if min < 10:
        min = f"0{min}"
    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(timer_text,text=f"{min}:{sec}")
    if t > 0:
        my_timer = window.after(1000,timer,t-1)
    else:
        start_timer()
        for i in range(math.floor(reps/2)):
            mark += "✔ "
        check_mark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50 , bg= YELLOW)


time_lb = Label(text="Timer" , font=(FONT_NAME , 45 , "bold",), fg=GREEN , bg=YELLOW)
time_lb.grid(column=1,row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image= img)
timer_text = canvas.create_text(102, 135, text="00:00", fill="white", font=(FONT_NAME , 35 , "bold",))
canvas.grid(column=1,row=1)


start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)
reset_button = Button(text="Reset",highlightthickness=0, command=reset_time)
reset_button.grid(column=2,row=2)

check_mark= Label(font=(FONT_NAME , 25 , "bold",), fg=GREEN , bg=YELLOW)
check_mark.grid(column=1,row=3)


window.mainloop()