from tkinter import *

# App Constants
WORK = 25
SHORT_BREAK = 5
LONG_BREAK = 20
BG_COLOR = "#222831"

# App Interface
interface = Tk()
interface.title("A3AJAGBE POMODORO APP")
interface.config(padx=100, pady=50, bg=BG_COLOR)

# Add background image using canvas widget
canvas = Canvas(width=160, height=130, bg=BG_COLOR, highlightthickness=0)
bg_image = PhotoImage(file="pomodoro_image.png")
canvas.create_image(80, 65, image=bg_image)
canvas.create_text(80, 75, text="00:00", fill="white", font=("Arial", 40, "bold"))
canvas.pack()

# Keep the app open until exited
interface.mainloop()
