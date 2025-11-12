# 💬 Rule-Based Chatbot App

A simple **Rule-Based Chatbot** built using **Python** and **Flask**.  
This chatbot responds to user messages based on predefined rules — no machine learning involved!  
It’s a great beginner project to understand how chatbots work and how Flask handles web requests.

---

## 🚀 Features

✅ Responds to greetings and basic questions  
✅ Displays the current time  
✅ User-friendly web interface (HTML, CSS, JavaScript)  
✅ Easy to customize chatbot responses in `rules.py`  
✅ Simple Flask backend for handling user input/output  

---

## 🧠 How It Works

This chatbot uses a **rule-based system** — meaning it checks the user’s message and replies based on pre-defined keywords.

Example:
- If the user says “hello”, the bot replies “Hi there! How can I help you today?”
- If the user asks for the time, the bot shows the current time.
- If the input doesn’t match any rule, it says: *“I'm sorry, I don't understand that yet.”*

---

## 🏗️ Project Structure
chatbot_app/
│
├── app.py # Flask backend
├── rules.py # Chatbot rules and responses
│
├── templates/
│ └── index.html # Frontend HTML page
│
└── static/
└── style.css # CSS styling

---

## ⚙️ Installation & Setup

### 1️⃣ Clone or download this repository
```bash
git clone https://github.com/<your-username>/chatbot_app.git
cd chatbot_app


Install dependencies
pip install flask

Run the Flask app
python app.py


