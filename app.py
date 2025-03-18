from flask import Flask, render_template, request, redirect, url_for, session
import project  # Importerer din eksisterende quiz-logikk

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Nødvendig for å håndtere session

# Simulerer en terminal-stil med CSS
terminal_style = """
body {
    background-color: black;
    color: white;
    font-family: monospace;
    padding: 20px;
}
input, button {
    background-color: black;
    color: white;
    border: 1px solid white;
    font-family: monospace;
    padding: 5px;
}
button:hover {
    background-color: gray;
}
"""

@app.route("/", methods=["GET", "POST"])
def login():
    """Login page"""
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "PGR107" and password == "Python":
            session["logged_in"] = True
            return redirect(url_for("quiz"))
        else:
            error = "❌ Invalid username or password. Try again."

    return render_template("login.html", error=error, terminal_style=terminal_style)


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    """Quiz page"""
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    if "current_question" not in session:
        session["current_question"] = 1
        session["correct_answers"] = 0
        session["incorrect_answers"] = []

    question_id = session["current_question"]

    if question_id > len(project.quiz_questions):
        return redirect(url_for("result"))

    question_data = project.quiz_questions[question_id]

    if request.method == "POST":
        user_answer = request.form["answer"].strip().lower()
        correct_answer = question_data["answer"]

        if user_answer == correct_answer:
            session["correct_answers"] += 1
        else:
            session["incorrect_answers"].append({
                "question": question_data["question"],
                "your_answer": f"{user_answer} ({question_data['options'].get(user_answer, 'Invalid choice')})",
                "correct_answer": f"{correct_answer} ({question_data['options'][correct_answer]})"
            })

        session["current_question"] += 1
        return redirect(url_for("quiz"))

    return render_template("quiz.html", question=question_data, question_id=question_id, terminal_style=terminal_style)


@app.route("/result")
def result():
    """Result page"""
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    return render_template("result.html", correct=session["correct_answers"],
                           incorrect=session["incorrect_answers"], terminal_style=terminal_style)


@app.route("/logout")
def logout():
    """Logout function"""
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
