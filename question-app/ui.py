
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Application")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(self.window, text="Score:", bg=THEME_COLOR, fg="white" ,font=("Arial", 18))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125,width=280, text="some text questions" ,
                                                     fill=THEME_COLOR, font=("Arial", 20))
        self.canvas.grid(row=1, column=0 ,columnspan=2, pady=30)

        true_page = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_page,highlightthickness=0,bd=0,command=self.true_buttons)
        self.true_button.grid(row=2, column=0)

        false_page = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_page,highlightthickness=0,command=self.false_buttons)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text ,text="you have reached the end of the questions")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_buttons(self):
        self.feed_back(self.quiz.check_answer("True"))

    def false_buttons(self):
        is_right = self.quiz.check_answer("False")
        self.feed_back(is_right)

    def feed_back(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
