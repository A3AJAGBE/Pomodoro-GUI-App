from tkinter import *
import math

# App Constants
WORK = 1
SHORT_BREAK = 5
LONG_BREAK = 20
BG_COLOR = "#222831"
FONT = "Courier"
timer_repeat = 0


def count_down(count):
    """This function counts down the timer"""
    # Set up the time display
    minutes = math.floor(count / 60)
    seconds = count % 60

    if minutes < 10:
        minutes = f"0{minutes}"

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        interface.after(1000, count_down, count - 1)
    else:
        start_timer()


def start_timer():
    """This function calls the countdown function"""
    global timer_repeat
    timer_repeat += 1
    work_sec = WORK * 60
    short_break_sec = SHORT_BREAK * 60
    long_break_sec = LONG_BREAK * 60

    if timer_repeat % 8 == 0:
        count_down(long_break_sec)
    elif timer_repeat % 2 == 0:
        count_down(short_break_sec)
    else:
        count_down(work_sec)


# App Interface
interface = Tk()
interface.title("A3AJAGBE POMODORO APP")
interface.config(padx=100, pady=50, bg=BG_COLOR)

timer = Label(text="Timer", fg="#f05454", bg=BG_COLOR, font=(FONT, 60, "bold"))
timer.grid(column=1, row=0)

# Add background image using canvas widget
canvas = Canvas(width=160, height=130, bg=BG_COLOR, highlightthickness=0)
bg_image = PhotoImage(file="pomodoro_image.png")
canvas.create_image(80, 65, image=bg_image)
timer_text = canvas.create_text(80, 75, text="00:00", fill="white", font=(FONT, 40, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0)
reset.grid(column=2, row=2)

check = Label(text="✅", bg=BG_COLOR)
check.grid(column=1, row=3)

# Keep the app open until exited
interface.mainloop()
