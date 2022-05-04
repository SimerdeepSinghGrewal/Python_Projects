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
REPS = 0
TICK = "✔"
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global REPS, TICK, TIMER
    TICK = "✔"
    REPS = 0
    window.after_cancel(TIMER)
    tick_label.config(text=" ")
    canvas.itemconfig(timer_text, text="00:00")
    main_label.config(text="Timer", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    global TICK
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS == 8:
        REPS = 0
        count_down(long_break_sec)
        main_label.config(text="Break", fg=RED)
    elif REPS % 2 == 0 and REPS != 8:
        count_down(short_break_sec)
        main_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        main_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global TICK
    global REPS
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(10, count_down, count - 1)
    else:
        start_timer()
        if REPS == 1:
            TICK = "✔"
        if REPS % 2 == 0:
            tick_label.config(text=TICK)
            TICK = TICK + "✔"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

main_label = Label(text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40))
main_label.grid(column=1, row=0)
start_button = Button(text="Start", width=10, bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", width=10, bg=YELLOW, highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)
tick_label = Label(fg=GREEN, bg=YELLOW)
tick_label.grid(column=1, row=3)

window.mainloop()
