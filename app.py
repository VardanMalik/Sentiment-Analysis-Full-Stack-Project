from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key for production

# Temporary in-memory storage for feedback; replace with a database as needed.
feedback_list = []

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

        feedback_list.append({'name': name, 'email': email, 'message': message})
        flash('Feedback submitted successfully', 'success')
        return redirect(url_for('feedback'))

    return render_template('feedback.html', feedback_list=feedback_list)

if __name__ == '__main__':
    app.run(debug=True)