import tkinter as tk
from tkinter import messagebox
import random

TOPIC = "Python Basics"


def get_ai_question(topic):
    questions = [
        {
            "question": "What does the print() function do in Python?",
            "options": [
                "Takes input from user",
                "Displays output on the screen",
                "Stops the program",
                "Creates a variable"
            ],
            "answer": "Displays output on the screen"
        },
        {
            "question": "Which symbol is used for comments in Python?",
            "options": ["//", "<!-- -->", "#", "/* */"],
            "answer": "#"
        },
        {
            "question": "What is the correct file extension for Python files?",
            "options": [".python", ".pt", ".py", ".p"],
            "answer": ".py"
        }
    ]

    return random.choice(questions)


class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Python Quiz Game")
        self.root.geometry("600x400")

        self.score = 0
        self.current_question = None

        self.create_ui()
        self.load_question()

    def create_ui(self):
        self.title_label = tk.Label(self.root, text="AI Python Quiz", font=("Arial", 18, "bold"))
        self.title_label.pack(pady=10)

        self.question_label = tk.Label(self.root, text="", font=("Arial", 14), wraplength=500)
        self.question_label.pack(pady=20)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(self.root, text="", width=40, font=("Arial", 12), command=lambda b=i: self.check_answer(b))
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.score_label = tk.Label(self.root, text="Score: 0", font=("Arial", 12, "bold"))
        self.score_label.pack(pady=10)

    def load_question(self):
        self.current_question = get_ai_question(TOPIC)
        self.question_label.config(text=self.current_question["question"])

        for i, option in enumerate(self.current_question["options"]):
            self.buttons[i].config(text=option)

    def check_answer(self, index):
        selected = self.buttons[index].cget("text")
        correct = self.current_question["answer"]

        if selected == correct:
            self.score += 1
            messagebox.showinfo("Correct", "Correct answer! ✅")
        else:
            messagebox.showerror("Wrong", f"Wrong answer ❌\nCorrect answer: {correct}")

        self.score_label.config(text=f"Score: {self.score}")
        self.load_question()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
