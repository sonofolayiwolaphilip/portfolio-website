from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    # Placeholder for actual email functionality
    print(f"Message from {name} ({email}): {message}")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
