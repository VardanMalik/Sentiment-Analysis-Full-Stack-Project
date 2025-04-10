# 🏋️ Vardan's Gym Website + Sentiment Feedback System

A modern gym website with a built-in feedback system that collects user reviews and performs real-time sentiment analysis using NLTK's VADER tool. This platform helps gym owners understand customer satisfaction through automated insights.

---

## 📸 Screenshots

> _Live demo of the project UI and dashboard_

- 🏠 Home Page  
  ![Home Page](screenshots/home.png)

- 📝 Feedback Form  
  ![Feedback Form](screenshots/feedback-form.png)

- 📊 Sentiment Dashboard  
  ![Sentiment Dashboard](screenshots/sentiment-analysis.png)

---

## 💡 Features

✅ Clean, responsive gym landing page  
✅ Feedback form with name, email, and message fields  
✅ Feedback is saved in a CSV file (`feedback.csv`)  
✅ Real-time sentiment analysis using VADER  
✅ Chart.js bar chart shows sentiment breakdown  
✅ Flash messages for form validation  
✅ Sentiment dashboard accessible at `/sentiment`

---

## 📂 Project Structure

gym-website/
├── app.py
├── feedback.csv               # Stores submitted feedback
├── static/                    # CSS, JS, images
│   ├── css/style.css
│   ├── js/script.js
│   └── images/
├── templates/                 # HTML files
│   ├── base.html
│   ├── index.html
│   ├── feedback.html
│   └── sentiment.html
├── venv/                      # Python virtual environment (optional)
└── README.md

---

## 🚀 How to Run Locally

### 1. Clone this repo

```bash
git clone https://github.com/VardanMalik/Sentiment-Analysis-for-targeted-Digital-Marketing-.git
cd gym-website
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate     # or venv\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### If requirements.txt doesn’t exist, manually install:

```bash
pip install flask pandas nltk
python3
>>> import nltk
>>> nltk.download('vader_lexicon')
>>> exit()
```

### 4. Run the app

```bash
python3 app.py
```

#### Visit http://localhost:5000

---

## 🔮 What Can Be Improved in the Future

- 🔐 **Password-Protected Admin Page**  
  Restrict access to the sentiment dashboard `/sentiment` using Flask login or a hardcoded password.

- 📤 **Export Sentiment Results**  
  Allow the admin to export analysis data as CSV or PDF reports.

- 📅 **Filter by Date**  
  Let the admin view feedback from specific weeks/months.

- 🌐 **Deploy Online**  
  Host the website using Render, Heroku, or Vercel for live access.

- ✨ **AI-Based Suggestions**  
  Automatically suggest actions based on negative feedback trends.

---

## 🧰 Tech Stack

- Python + Flask  
- NLTK (VADER Sentiment Analyzer)  
- Chart.js (for visualization)  
- HTML5 + CSS3  
- JavaScript  
- SQLite / CSV for data storage

---

## ⚙️ Requirements

- Python 3.10+  
- `nltk`, `flask`, `pandas`

---

## 📄 License

© 2025 Vardan Malik  
Licensed under the Apache License, Version 2.0 (the "License");  
you may not use this file except in compliance with the License.  
You may obtain a copy of the License at:

🔗 http://www.apache.org/licenses/LICENSE-2.0

Unless required by law or agreed to in writing, software  
distributed under the License is distributed on an "AS IS" BASIS,  
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.  
See the License for the specific language governing permissions and limitations under the License.

