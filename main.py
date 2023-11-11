import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style

# Create the main window
root = tk.Tk()
root.title("Quiz App")
root.geometry("600x500")
style = Style(theme="flatly")

# Create the feedback label
feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

quiz_data = [
    {
        "question": "What is the name of the law in India that protects the rights of children?",
        "choices": ["A: Child Safety Act", "B: Children's Rights Act", "C: Juvenile Justice Act", "D: Kid Protection Law"],
        "answer": "C"
    },
    {
        "question": "How old should you be to work in most jobs in India according to child labor laws?",
        "choices": ["A: 10 years old", "B: 14 years old", "C: 16 years old", "D: 18 years old"],
        "answer": "B"
    },
    {
        "question": "What is the right of every child to have a name and a nationality called?",
        "choices": ["A: Right to Education", "B: Right to Play", "C: Right to Identity", "D: Right to Food"],
        "answer": "C"
    },
    {
        "question": "Children have the right to be protected from all forms of violence, abuse, and neglect. Which organization in India helps ensure this right?",
        "choices": ["A: UNICEF", "B: Child Protection Agency", "C: Child Welfare Committee", "D: Kids' Rights Watch"],
        "answer": "C"
    },
    {
        "question": "What does the Right to Education mean for children in India?",
        "choices": ["A: The right to play", "B: The right to attend school and get an education", "C: The right to choose their own friends", "D: The right to work and earn money"],
        "answer": "B"
    },
    {
        "question": "What is the name of the national campaign in India that focuses on the welfare of girls and their right to live and thrive?",
        "choices": ["A: Save the Boys Campaign", "B: Beti Bachao Beti Padhao", "C: Children's Health Initiative", "D: Youth Empowerment Program"],
        "answer": "B"
    },
    {
        "question": "Which right ensures that children have access to clean drinking water, nutritious food, and a clean environment?",
        "choices": ["A: Right to Play", "B: Right to Education", "C: Right to Health", "D: Right to Freedom of Speech"],
        "answer": "C"
    },
    {
        "question": "What is the age up to which children in India have the right to receive free and compulsory education under the Right to Education Act?",
        "choices": ["A: 12 years", "B: 14 years", "C: 16 years", "D: 18 years"],
        "answer": "B"
    },
    {
        "question": "What is the maximum duration for which a child can be placed in a children's home or special home under the Juvenile Justice Act?",
        "choices": ["A: 1 year", "B: 3 years", "C: 5 years", "D: 10 years"],
        "answer": "B"
    },
    {
        "question": "According to the Juvenile Justice Act, what happens to children who commit crimes?",
        "choices": ["A: They are sent to adult prisons", "B: They are given a warning and released", "C: They are sent to juvenile homes for rehabilitation and support", "D: They are fined and made to do community service"],
        "answer": "C"
    },
]

# Function to move to the next question
def next_question():
    global current_question
    current_question += 1

    if current_question < len(quiz_data):
        # If there are more questions, show the next question
        show_question()
    else:
        # If all questions have been answered, display the final score and end the quiz
        messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))
        root.destroy()

# Create the next button
next_btn = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled"
)
next_btn.pack(pady=10)

# Function to display the current question and choices
def show_question():
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    # Clear the feedback label and disable the next button
    feedback_label.config(text="")
    next_btn.config(state="disabled")

    # Display the choices on the buttons
    for i in range(4):
        if i < len(question["choices"]):
            choice_btns[i].config(text=question["choices"][i], state="normal")
        else:
            choice_btns[i].config(text="", state="disabled")

    # Clear the selected choice
    selected_choice.set(None)

# Function to check the selected answer and provide feedback
def check_answer():
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    selected_index = selected_choice.get()

    if selected_index is None:
        # No option selected, show an error message
        messagebox.showerror("Error", "Please select an answer.")
    elif question["choices"][selected_index].startswith(question["answer"]):
        # Correct answer (checking if the selected choice starts with the correct answer)
        feedback_label.config(text="Correct!", foreground="green")
        # Update the score and display it
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
    else:
        # Incorrect answer
        feedback_label.config(text="Incorrect!", foreground="red")

    # Disable all choice buttons and enable the next button
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

# Initialize the current question index
current_question = 0

# Create the question label
qs_label = ttk.Label(
    root,
    anchor="center",
    wraplength=500,
    padding=10
)
qs_label.pack(pady=10)

# Initialize the selected choice variable
selected_choice = tk.IntVar()

# Create the choice buttons
choice_btns = []
for i in range(4):
    button = ttk.Radiobutton(
        root,
        variable=selected_choice,
        value=i,
        command=check_answer
    )
    button.pack(pady=5)
    choice_btns.append(button)

# Create the feedback label
feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

# Initialize the score
score = 0

# Create the score label
score_label = ttk.Label(
    root,
    text="Score: 0/{}".format(len(quiz_data)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)

# Show the first question
show_question()

# Start the main event loop
root.mainloop()