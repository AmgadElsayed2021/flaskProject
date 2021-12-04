import sqlite3
from Application import app
from flask import render_template,request
from contextlib import closing

# def get_db_connection():
conn = sqlite3.connect('database.sqlite', check_same_thread=False)
conn.row_factory = sqlite3.Row


@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html', index=True)# just make the index = true so i can use to style the nav button in the nav.html
# msg = ''
#     if request.method == 'POST' and 'username' in request.form and 'password' in request.form :
#         username = request.form['username']
#         password = request.form['password']
#         with closing(conn.cursor()) as c :
#             query=('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password,))
#             c.execute(query)
#         account = c.fetchone()
#
#         if account :
#             session['loggedin'] = True
#             session['id'] = account['id']
#             session['username'] = account['username']
#             msg = 'Logged in successfully !'
#             return render_template('index.html', msg=msg)
#         else :
#             msg = 'Incorrect username / password !'
#     return render_template('login.html', msg=msg)

@app.route('/login')
def login():
    return render_template('login.html',login=True)

@app.route('/categories')
def categories():
    with closing(conn.cursor()) as c :
        query = 'select distinct category from Books'
        c.execute(query)
        results = c.fetchall()
        categories = []
        for result in results :
            categories.append(result)


        query = 'select * from Books where category=?'
        c.execute(query,({{ categories}},))
        results = c.fetchall()
        category_books = []
        for result in results :
            category_books.append(result)
    return render_template('categories.html',category_books=category_books,categories=categories)

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