import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")

        self.choices = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.computer_score = 0

        # Styling
        self.root.configure(bg="#e0f7fa")  # Light Blue background

        self.create_widgets()

    def create_widgets(self):
        # Labels
        self.label = tk.Label(self.root, text="Choose Rock, Paper, or Scissors", font=("Helvetica", 14), bg="#e0f7fa")
        self.label.pack(pady=10)

        # Buttons
        button_style = {"font": ("Helvetica", 12), "width": 10, "height": 2, "bg": "#80deea", "activebackground": "#26c6da"}
        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play("rock"), **button_style)
        self.rock_button.pack(pady=5)

        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play("paper"), **button_style)
        self.paper_button.pack(pady=5)

        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play("scissors"), **button_style)
        self.scissors_button.pack(pady=5)

        # Score
        self.score_label = tk.Label(self.root, text="Score - You: 0 | Computer: 0", font=("Helvetica", 12), bg="#e0f7fa")
        self.score_label.pack(pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(user_choice, computer_choice)

        # Display result in a messagebox
        messagebox.showinfo("Result", result)

        # Update score label
        self.update_score_label()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'scissors' and computer_choice == 'paper') or
            (user_choice == 'paper' and computer_choice == 'rock')
        ):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "You lose!"

    def update_score_label(self):
        self.score_label.config(text=f"Score - You: {self.user_score} | Computer: {self.computer_score}")

def main():
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.geometry("400x300")  # Set the initial window size
    root.mainloop()

if __name__ == "__main__":
    main()
