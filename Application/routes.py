from Application import app
from flask import render_template
@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html',login=True)
@app.route('/login')
def login():
    return render_template('login.html',login=True)

@app.route('/categories')
def categories():
    return render_template('categories.html',login=True)
@app.route('/books')
def books():
    return render_template('books.html',login=True)
@app.route('/register')
def register():
    return render_template('register.html',login=True)