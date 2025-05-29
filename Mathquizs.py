import tkinter as tk
from tkinter import messagebox
import random
import operator

# Math operations
operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

class MathQuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("🧠 Maths Quiz")
        self.master.geometry("400x300")
        self.master.resizable(False, False)

        self.score = 0
        self.question_number = 0
        self.total_questions = 5
        self.name = ""

        self.question = ""
        self.answer = 0

        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self.master, text="Enter your name:")
        self.name_label.pack(pady=10)

        self.name_entry = tk.Entry(self.master)
        self.name_entry.pack(pady=5)

        self.start_button = tk.Button(self.master, text="Start Quiz", command=self.start_quiz)
        self.start_button.pack(pady=10)

        self.question_label = tk.Label(self.master, text="", font=("Helvetica", 14))
        self.answer_entry = tk.Entry(self.master)
        self.submit_button = tk.Button(self.master, text="Submit Answer", command=self.check_answer)
        self.feedback_label = tk.Label(self.master, text="", font=("Helvetica", 12))
        self.next_button = tk.Button(self.master, text="Next Question", command=self.next_question)

    def start_quiz(self):
        self.name = self.name_entry.get()
        if not self.name.strip():
            messagebox.showwarning("Warning", "Please enter your name.")
            return

        self.name_label.pack_forget()
        self.name_entry.pack_forget()
        self.start_button.pack_forget()
        self.next_question()

    def generate_question(self):
        op = random.choice(list(operations.keys()))
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        if op == "/":
            num1 *= num2  # Ensure exact division
        question_text = f"{num1} {op} {num2}"
        answer = round(operations[op](num1, num2), 2)
        return question_text, answer

    def next_question(self):
        self.feedback_label.pack_forget()
        self.answer_entry.delete(0, tk.END)

        if self.question_number >= self.total_questions:
            self.show_score()
            return

        self.question, self.answer = self.generate_question()
        self.question_number += 1

        self.question_label.config(text=f"Q{self.question_number}: What is {self.question}?")
        self.question_label.pack(pady=15)
        self.answer_entry.pack(pady=5)
        self.submit_button.pack(pady=5)

    def check_answer(self):
        try:
            user_ans = float(self.answer_entry.get())
            if abs(user_ans - self.answer) < 0.01:
                self.feedback_label.config(text="✅ Correct!", fg="green")
                self.score += 1
            else:
                self.feedback_label.config(text=f"❌ Wrong! Answer: {self.answer}", fg="red")
        except ValueError:
            self.feedback_label.config(text="⚠️ Please enter a valid number.", fg="orange")

        self.feedback_label.pack()
        self.submit_button.pack_forget()
        self.next_button.pack(pady=5)

    def show_score(self):
        self.question_label.pack_forget()
        self.answer_entry.pack_forget()
        self.next_button.pack_forget()
        self.feedback_label.pack_forget()

        final_msg = f"🎉 {self.name}, you scored {self.score}/{self.total_questions}"
        messagebox.showinfo("Quiz Completed!", final_msg)
        self.master.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuizApp(root)
    root.mainloop()
