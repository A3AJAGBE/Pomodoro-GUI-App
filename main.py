from tkinter import *

# App Constants
WORK = 25
SHORT_BREAK = 5
LONG_BREAK = 20
BG_COLOR = "#222831"
FONT = "Courier"

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
canvas.create_text(80, 75, text="00:00", fill="white", font=(FONT, 40, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", highlightthickness=0)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0)
reset.grid(column=2, row=2)

check = Label(text="✅", bg=BG_COLOR)
check.grid(column=1, row=3)

# Keep the app open until exited
interface.mainloop()
