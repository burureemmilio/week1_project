import random

# List of quiz questions
questions = [
    {
        "question": "What is the capital city of Kenya?",
        "choices": {
            "A": "Mombasa",
            "B": "Nairobi",
            "C": "Kisumu",
            "D": "Nakuru"
        },
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": {
            "A": "Earth",
            "B": "Jupiter",
            "C": "Mars",
            "D": "Venus"
        },
        "answer": "C"
    },
    {
        "question": "What is 8 × 7?",
        "choices": {
            "A": "54",
            "B": "56",
            "C": "64",
            "D": "49"
        },
        "answer": "B"
    },
    {
        "question": "Which language is mainly used to style web pages?",
        "choices": {
            "A": "HTML",
            "B": "Python",
            "C": "CSS",
            "D": "Java"
        },
        "answer": "C"
    },
    {
        "question": "How many days are there in a leap year?",
        "choices": {
            "A": "365",
            "B": "364",
            "C": "360",
            "D": "366"
        },
        "answer": "D"
    }
]


# Mix the order of the questions
random.shuffle(questions)

score = 0

print("WELCOME TO THE QUIZ")

# Loop through each question
for number, question in enumerate(questions, start=1):
    print(f"\nQuestion {number}: {question['question']}")

    # Display the choices
    for letter, choice in question["choices"].items():
        print(f"{letter}. {choice}")

     # Continue asking until the user enters A, B, C or D
    while True:
        try:
            user_answer = input("Enter your answer (A, B, C or D): ").upper()

            if user_answer not in ["A", "B", "C", "D"]:
                raise ValueError

            break

        except ValueError:
            print("Invalid input. Please enter A, B, C or D.")
    
    # Check whether the answer is correct
    if user_answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        correct_letter = question["answer"]
        correct_choice = question["choices"][correct_letter]

        print("Incorrect.")
        print(f"The correct answer is {correct_letter}. {correct_choice}")


# Display final score
total_questions = len(questions)

print(f"Your score is {score}/{total_questions}")

if score == 5:
    print("Excellent")
elif score == 4:
    print("Very Good")
elif score == 3:  
    print("Good")
elif score == 2:
    print("Nice Try")
else:
    print("Try Again")              
