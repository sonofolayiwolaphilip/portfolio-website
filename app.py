from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from projects import projects
from os import getenv

app = Flask(__name__)

# Flask Config from .env
app.secret_key = getenv('SECRET_KEY')

# Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = getenv('MAIL_USERNAME')

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html', projects=projects)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if not name or not email or not message:
            flash("All fields are required!", "danger")
            return redirect(url_for('contact'))

        # Send email
        try:
            msg = Message(
                subject=f"New Message from {name}",
                sender=email,
                recipients=[app.config['MAIL_USERNAME']],
                body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            )
            mail.send(msg)
            flash("Message sent successfully!", "success")
        except Exception as e:
            flash(f"Failed to send message: {e}", "danger")

        return redirect(url_for('contact'))
    
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
