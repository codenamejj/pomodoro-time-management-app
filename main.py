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
our_check = "✅"
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    global our_check
    our_check = ""
    global reps
    reps = 0
    check_label.config(text=our_check, bg=YELLOW, fg=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    print(reps)

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="Long Break", fg=PINK, font=FONT_NAME)
        countdown(long_break_seconds)

    elif reps % 2 == 0 and reps > 1 < 8:
        title_label.config(text="Short Break", fg=PINK, font=FONT_NAME)
        countdown(short_break_seconds)

    elif reps % 2 != 0 and reps < 9:
        title_label.config(text="Work", fg=GREEN, font=FONT_NAME)
        countdown(work_seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(count):
    # print(minutes)
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    elif count_min < 10:
        count_sec = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1, countdown, count - 1)
    else:
        start_timer()

        if reps % 2 == 0:
            global our_check
            our_check += "✅"
            check_label.config(text=our_check, bg=YELLOW, fg=GREEN)

            print(our_check)





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# window.minsize(width=600, height=500)
window.maxsize(width=500, height=500)

title_label = Label()
title_label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 45), bg=YELLOW, highlightthickness=0)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image =tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button()
start_button.config(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

check_label = Label()
check_label.config(bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=2)

reset_button = Button()
reset_button.config(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
