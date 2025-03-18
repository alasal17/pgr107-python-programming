# 🏫 PGR107 – Python Programming | Kristiania University College

## 🎯 Multiple Choice Quiz (Flask Web App)

This project is a web-based multiple-choice quiz about Norway, developed as part of **PGR107 – Python Programming** at **Kristiania University College**.

Users must log in with a predefined **username** and **password** and then answer **10 multiple-choice questions**. The application tracks correct and incorrect answers and provides a summary at the end.

---

## 🌍 **Live Demo**
Test the web application here:  
🔗 **[Quiz Game Web App](https://quiz-game.anez.no/)**

**🔑 Login credentials for testing:**  
- **Username:** `PGR107`  
- **Password:** `Python`  

---

## 🛠 **Features**
✅ **Web-based terminal style** – Mimics a terminal-like experience in a web browser  
✅ **Secure login system** – Only users with correct credentials can access the quiz  
✅ **10 multiple-choice questions** – Focused on Norwegian facts  
✅ **Input validation** – Users must select a valid answer  
✅ **Results page** – Displays the number of correct/incorrect answers and a detailed error summary  
✅ **Supports multiple users simultaneously** via Flask sessions  
✅ **Hosted on Heroku** – Accessible from anywhere  

---

## 📦 **Technologies Used**
- **Python** (Flask)
- **HTML/CSS** (Bootstrap for basic styling)
- **Jinja2** (For dynamic content in HTML)
- **Heroku** (For hosting the application)

---

## 🏗 **Installation and Running Locally**
If you want to run the application locally, follow these steps:

### 1️⃣ **Clone the repository**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2️⃣ **Install dependencies**
Ensure you have Python installed, then install Flask and required packages:
```bash
pip install -r requirements.txt
```

### 3️⃣ **Start the Flask server**
```bash
python app.py
```
Then, open your browser and go to:
```
http://127.0.0.1:5000/
```

---

## 🚀 **Deploying on Heroku**
### 1️⃣ **Log in to Heroku**
```bash
heroku login
```

### 2️⃣ **Create a new Heroku app**
```bash
heroku create quiz-game-anez
```

### 3️⃣ **Add Heroku remote and push the code**
```bash
git init
git add .
git commit -m "Deploy Flask quiz app"
git push heroku main
```

### 4️⃣ **Scale the web process**
```bash
heroku ps:scale web=1
```

### 5️⃣ **Open the application**
```bash
heroku open
```

---

## 📜 **Project Structure**
```
📂 project-folder
│── app.py             # Flask web server
│── project.py         # Original quiz logic
│── requirements.txt   # Dependencies
│── Procfile           # Heroku configuration
│── templates/         # HTML frontend templates
│   │── login.html
│   │── quiz.html
│   │── result.html
```

---
