"""
=========================================================
PGR107 – Python Programming | Høyskolen Kristiania
Programming Project – Multiple Choice Quiz
=========================================================
Author  : Salam Alanezy
Date    : 18.03.2025
School  : Høyskolen Kristiania
Course  : PGR107 – Python Programming
Project : Multiple Choice Quiz
Due Date: 23.03.2025  23:59

Features:
- Secure login system with username and password verification.
- Includes an ASCII logo for improved UI.
- Uses terminal colors for better readability.
- Ensures only valid user input is accepted (login and quiz).
- Asks 10 multiple-choice questions about Norway.
- Handles invalid answers by prompting user until a valid choice is given.
- Displays the number of correct and incorrect answers at the end.
- Provides a detailed summary of incorrect answers (question, user response, correct answer).

Guidelines:
- Follows the exact project requirements, including login validation, quiz flow, and result summary.
- Uses only approved Python topics (dictionaries, loops, functions, input handling).
- Ensures correct error handling and input validation to prevent crashes.
- No object-oriented programming (OOP) or external libraries used.
- The entire program is contained in a single Python file for submission.

=========================================================
"""


COLORS = {
    "black": "\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green": "\033[0;32m",
    "yellow": "\u001b[33;1m",
    "blue": "\u001b[34;1m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "reset": "\u001b[0m"
}

def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

def print_ascii_logo():
    ascii_logo = r"""
[[cyan]]
   ____        _        _____                      
  / __ \      (_)      / ____|                     
 | |  | |_   _ _ ____ | |  __  __ _ _ __ ___   ___ 
 | |  | | | | | |_  / | | |_ |/ _` | '_ ` _ \ / _ \\
 | |__| | |_| | |/ /  | |__| | (_| | | | | | |  __/
  \_____\__,_|_/___|  \_____|\__,_|_| |_| |_|\___|
                                                   
[[yellow]] Welcome to the Quiz Game! [[reset]]
    """
    print(colorText(ascii_logo))


def login_info():

    correct_credentials = {'username': 'PGR107', 'password': 'Python'}

    while True:
        username = input(colorText("🔑 [[yellow]]Enter username: [[reset]]"))
        password = input(colorText("🔒 [[yellow]]Enter password: [[reset]]"))

        if username == correct_credentials['username'] and password == correct_credentials['password']:
            print(colorText("✅ [[green]]User 'PGR107' is successfully logged in![[reset]]"))
            print(colorText("\n🚀 [[blue]]Starting the quiz... Good luck![[reset]]\n"))
            return True  # Successful login

        else:
            print(colorText("❌ [[red]]Invalid username and/or password. Please try again.[[reset]]"))


quiz_questions = {
    1: {
        "question": "What is the capital of Norway?",
        "options": {"a": "Bergen", "b": "Oslo", "c": "Stavanger", "d": "Trondheim"},
        "answer": "b"
    },
    2: {
        "question": "What is the currency of Norway?",
        "options": {"a": "Euro", "b": "Pound", "c": "Krone", "d": "Deutsche Mark"},
        "answer": "c"
    },
    3: {
        "question": "What is the largest city in Norway?",
        "options": {"a": "Oslo", "b": "Stavanger", "c": "Bergen", "d": "Trondheim"},
        "answer": "a"
    },
    4: {
        "question": "When is constitution day (the national day) of Norway?",
        "options": {"a": "27th May", "b": "17th May", "c": "17th April", "d": "27th April"},
        "answer": "b"
    },
    5: {
        "question": "What color is the background of the Norwegian flag?",
        "options": {"a": "Red", "b": "White", "c": "Blue", "d": "Yellow"},
        "answer": "a"
    },
    6: {
        "question": "How many countries does Norway border?",
        "options": {"a": "1", "b": "2", "c": "3", "d": "4"},
        "answer": "c"
    },
    7: {
        "question": "What is the name of the university in Trondheim?",
        "options": {"a": "UiS", "b": "UiO", "c": "NMBU", "d": "NTNU"},
        "answer": "d"
    },
    8: {
        "question": "How long is the border between Norway and Russia?",
        "options": {"a": "96 km", "b": "196 km", "c": "296 km", "d": "396 km"},
        "answer": "b"
    },
    9: {
        "question": "Where in Norway is Stavanger?",
        "options": {"a": "North", "b": "South", "c": "South-west", "d": "South-east"},
        "answer": "c"
    },
    10: {
        "question": "From which Norwegian city did the world’s famous composer Edvard Grieg come?",
        "options": {"a": "Oslo", "b": "Bergen", "c": "Stavanger", "d": "Tromsø"},
        "answer": "b"
    }
}


def quiz_logic():
    correct_answers = 0
    incorrect_answers = []

    for q_num, q_data in quiz_questions.items():
        print(colorText(f"\n🎯 [[cyan]]Question {q_num}: {q_data['question']}[[reset]]"))

        for option, answer in q_data["options"].items():
            print(f"   {option}. {answer}")

        while True:
            user_answer = input(colorText("💡 [[yellow]]Enter your answer (a, b, c, d): [[reset]]")).strip().lower()

            if user_answer in q_data["options"]:
                break
            else:
                print(colorText("⚠️ [[red]]Invalid choice! Please enter one of the available options (a, b, c, or d).[[reset]]"))


        if user_answer == q_data["answer"]:
            print(colorText("✅ [[green]]Correct![[reset]]"))
            correct_answers += 1
        else:
            print(colorText("❌ [[red]]Incorrect![[reset]]"))
            incorrect_answers.append({
                "question": q_data["question"],
                "your_answer": f"{user_answer} ({q_data['options'].get(user_answer, 'Invalid choice')})",
                "correct_answer": f"{q_data['answer']} ({q_data['options'][q_data['answer']]})"
            })

    print(colorText("\n🎯 [[yellow]]Quiz Complete![[reset]]"))
    print(colorText(f"✅ [[green]]Correct answers: {correct_answers}/{len(quiz_questions)}[[reset]]"))
    print(colorText(f"❌ [[red]]Incorrect answers: {len(incorrect_answers)}/{len(quiz_questions)}[[reset]]"))

    if incorrect_answers:
        print(colorText("\n📌 [[magenta]]Incorrect Answers Summary:[[reset]]"))
        for error in incorrect_answers:
            print(colorText(f"\n📖 Question: {error['question']}"))
            print(colorText(f"❌ Your answer: {error['your_answer']}"))
            print(colorText(f"✅ Correct answer: {error['correct_answer']}"))

def main():
    print_ascii_logo()  # Display ASCII logo

    # Run the login system
    if login_info():
        print(colorText(f"\n🎉 [[cyan]]Login successful! Starting the quiz now...[[reset]]\n"))
        quiz_logic()  # Start the quiz

