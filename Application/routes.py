import sqlite3
from Application import app
from flask import render_template,request


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html',index=True)# just make the index = true so i can use to style the nav button in the nav.html

@app.route('/login')
def login():
    return render_template('login.html',login=True)

@app.route('/categories')
def categories():
    return render_template('categories.html',categories=True)
@app.route('/books')
def books():
    return render_template('books.html',books=True)
@app.route('/register')
def register():
    return render_template('register.html',register=True)