from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.num = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some question text here.",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true = PhotoImage(file="images/true.png")
        false = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true, highlightthickness=0, bg=THEME_COLOR,
                                  command=self.true_press)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=false, highlightthickness=0, bg=THEME_COLOR,
                                   command=self.false_press)
        self.false_button.grid(column=1, row=2)

        self.score_label = Label(text="Score : 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question)
        else:
            self.canvas.itemconfig(self.question,
                                   text=f"You have reached the end of the quiz. Your score is {self.score} out of {self.num}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_press(self):
        right = self.quiz.check_answer("true")
        self.feedback(right)

    def false_press(self):
        right = self.quiz.check_answer("false")
        self.feedback(right)

    def feedback(self, right):
        if right:
            self.score += 1
            self.num += 1
            self.score_label.config(text=f"Score : {self.score}/{self.num}")
            self.canvas.config(bg="green")
        elif not right:
            self.num += 1
            self.score_label.config(text=f"Score : {self.score}/{self.num}")
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)
