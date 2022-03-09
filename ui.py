from tkinter import *

THEME_COLOR = "#375362"
FONT = "Arial"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=30, pady=30, bg=THEME_COLOR)

        # Score Label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=(FONT, 10))
        self.score_label.grid(column=1, row=0)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0, )
        self.canvas.grid(column=0, row=1, columnspan=2, padx=0, pady=50)
        self.question_text = self.canvas.create_text(150, 125, text=f"Testing text", fill=THEME_COLOR,  font=(FONT, 20, "italic"), )

        # buttons
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, bg=THEME_COLOR, highlightthickness=0, padx=20, pady=20)
        self.true_button.grid(column=0, row=3)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, bg=THEME_COLOR, highlightthickness=0, padx=20, pady=20)
        self.false_button.grid(column=1, row=3)

        self.window.mainloop()
