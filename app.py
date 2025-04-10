from flask import Flask, render_template, request, redirect, url_for, flash
import csv
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

FEEDBACK_FILE = 'feedback.csv'

# Ensure file exists and has headers
if not os.path.exists(FEEDBACK_FILE):
    with open(FEEDBACK_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'email', 'message'])

def read_feedback():
    feedback_data = []
    with open(FEEDBACK_FILE, newline='') as file:
        reader = csv.DictReader(file)
        feedback_data = list(reader)
    return feedback_data[::-1]  # reverse to show latest first

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
            flash('All fields are required', 'danger')
            return redirect(url_for('feedback'))

        # Save to CSV file
        with open(FEEDBACK_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, email, message])

        flash('Feedback submitted successfully', 'success')
        return redirect(url_for('feedback'))

    feedback_list = read_feedback()
    return render_template('feedback.html', feedback_list=feedback_list)

if __name__ == '__main__':
    app.run(debug=True)