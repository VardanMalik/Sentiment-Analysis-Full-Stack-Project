from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, desc
from datetime import datetime
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:your_strong_password@localhost/gym_feedback'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
analyzer = SentimentIntensityAnalyzer()

# Feedback Model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    sentiment = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    avg_rating = db.session.query(func.avg(Feedback.rating)).scalar()
    top_feedback = Feedback.query.filter_by(sentiment='Positive').order_by(desc(Feedback.rating)).limit(3).all()
    return render_template('index.html', avg_rating=round(avg_rating or 0, 1), top_feedback=top_feedback)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        rating = int(request.form['rating'])

        score = analyzer.polarity_scores(message)['compound']
        if score >= 0.05:
            sentiment = 'Positive'
        elif score <= -0.05:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'

        entry = Feedback(name=name, email=email, message=message, rating=rating, sentiment=sentiment)
        db.session.add(entry)
        db.session.commit()

        flash('Thank you for your feedback!', 'success')
        return redirect(url_for('feedback'))

    feedback_list = Feedback.query.order_by(Feedback.created_at.desc()).all()
    return render_template('feedback.html', feedback_list=feedback_list)

@app.route('/admin')
def admin():
    feedbacks = Feedback.query.all()
    sentiment_counts = {
        'Positive': Feedback.query.filter_by(sentiment='Positive').count(),
        'Neutral': Feedback.query.filter_by(sentiment='Neutral').count(),
        'Negative': Feedback.query.filter_by(sentiment='Negative').count(),
    }
    ratings = db.session.query(Feedback.rating, func.count(Feedback.rating)).group_by(Feedback.rating).all()
    return render_template('admin.html', feedbacks=feedbacks, sentiments=sentiment_counts, ratings=ratings)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
