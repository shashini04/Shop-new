from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample users dictionary (for demonstration purposes, in a real app, use a database)
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if username already exists
        if username in users:
            return render_template('register.html', message='Username already exists. Please choose another one.')
        users[username] = password
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
