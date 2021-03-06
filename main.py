from tkinter import *
import math
import beepy

# App Constants
WORK = 25
SHORT_BREAK = 5
LONG_BREAK = 20
BG_COLOR = "#222831"
FONT = ("Courier", 50, "bold")
timer_repeat = 0
timer = None


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
        global timer
        timer = interface.after(1000, count_down, count - 1)
    else:
        start_timer()
        add_check = ""
        sessions = math.floor(timer_repeat/2)
        for _ in range(sessions):
            add_check += "✅"
        checks.config(text=add_check)


def start_timer():
    """This function calls the countdown function"""
    global timer_repeat
    timer_repeat += 1
    work_sec = WORK * 60
    short_break_sec = SHORT_BREAK * 60
    long_break_sec = LONG_BREAK * 60

    if timer_repeat % 8 == 0:
        beepy.beep(sound='ready')
        count_down(long_break_sec)
        timer_label.config(text="Long Break")
    elif timer_repeat % 2 == 0:
        beepy.beep(sound='coin')
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg="#cdb30c")
    else:
        beepy.beep(sound='ping')
        count_down(work_sec)
        timer_label.config(text="Work Timer", fg="#28df99")


def reset_timer():
    """This function clears the timer"""
    interface.after_cancel(timer)
    beepy.beep(sound='error')
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Start Timer")
    checks.config(text="")
    global timer_repeat
    timer_repeat = 0


# App Interface
interface = Tk()
interface.title("A3AJAGBE POMODORO APP")
interface.config(padx=100, pady=50, bg=BG_COLOR)

timer_label = Label(text="Start Timer", fg="#f05454", bg=BG_COLOR, font=FONT)
timer_label.grid(column=1, row=0)

# Add background image using canvas widget
canvas = Canvas(width=160, height=130, bg=BG_COLOR, highlightthickness=0)
bg_image = PhotoImage(file="pomodoro_image.png")
canvas.create_image(80, 65, image=bg_image)
timer_text = canvas.create_text(80, 75, text="00:00", fill="white", font=FONT)
canvas.grid(column=1, row=1)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

checks = Label(bg=BG_COLOR)
checks.grid(column=1, row=3)

# Keep the app open until exited
interface.mainloop()
