from flask import Flask, render_template, request, redirect, url_for, flash
import csv
import os
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this for production

FEEDBACK_FILE = 'feedback.csv'
analyzer = SentimentIntensityAnalyzer()

# Make sure feedback.csv exists and has headers
if not os.path.exists(FEEDBACK_FILE):
    with open(FEEDBACK_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'email', 'message'])

# Helper function to read CSV into list of dicts
def read_feedback():
    with open(FEEDBACK_FILE, newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)[::-1]  # Show latest first

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if not name or not email or not message:
            flash('All fields are required.', 'danger')
            return redirect(url_for('feedback'))

        with open(FEEDBACK_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, email, message])

        flash('Feedback submitted successfully!', 'success')
        return redirect(url_for('feedback'))

    feedback_list = read_feedback()
    return render_template('feedback.html', feedback_list=feedback_list)

@app.route('/sentiment')
def sentiment():
    try:
        df = pd.read_csv(FEEDBACK_FILE)
    except FileNotFoundError:
        flash("No feedback found yet.", "danger")
        return redirect(url_for('feedback'))

    sentiments = {'Positive': 0, 'Neutral': 0, 'Negative': 0}

    for message in df['message']:
        score = analyzer.polarity_scores(message)['compound']
        if score >= 0.05:
            sentiments['Positive'] += 1
        elif score <= -0.05:
            sentiments['Negative'] += 1
        else:
            sentiments['Neutral'] += 1

    return render_template('sentiment.html', sentiments=sentiments)

if __name__ == '__main__':
    app.run(debug=True)