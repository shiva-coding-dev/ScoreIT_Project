from flask import Flask, render_template
app = Flask(__name__)

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/')
def home_page():
    return render_template('home.html')