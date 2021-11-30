import sqlite3
from Application import app
from flask import render_template,request
from contextlib import closing

# def get_db_connection():
conn = sqlite3.connect('database.sqlite', check_same_thread=False)


@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html', index=True)# just make the index = true so i can use to style the nav button in the nav.html

@app.route('/login')
def login():
    return render_template('login.html',login=True)

@app.route('/categories')
def categories():
    return render_template('categories.html',categories=True)

@app.route('/books')
def books():
    # images=['murach java.png','pacific.jpg']
    with closing(conn.cursor())as c:
        query= 'select * from Books'
        c.execute(query)
        results = c.fetchall()
        books=[]
        for result in results:
            books.append(result)
    return render_template('books.html',books=books)


@app.route('/register')
def register():
    return render_template('register.html',register=True)