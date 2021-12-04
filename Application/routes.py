import sqlite3
from Application import app
from flask import render_template, request, session
from contextlib import closing

# def get_db_connection():
conn = sqlite3.connect('database.sqlite', check_same_thread=False)
conn.row_factory = sqlite3.Row


@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html', index=True)# just make the index = true so i can use to style the nav button in the nav.html


@app.route('/login',methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form :
        email = request.form['email']
        password = request.form['password']
        with closing(conn.cursor()) as c :
            c.execute('SELECT * FROM accounts WHERE email = ? AND password = ?', (email, password,))
            account = c.fetchone()

        if account :
            session['loggedin'] = True
            session['id'] = account['id']
            session['email'] = account['email']
            msg = 'Logged in successfully !'
            return render_template('index.html', msg=msg)
        else :
            msg = 'Incorrect email / password !'
    return render_template('login.html', msg=msg)



@app.route('/categories',methods =['GET', 'POST'])
def categories():
    with closing(conn.cursor()) as c :
        query = 'select distinct category from Books'
        c.execute(query)
        results = c.fetchall()
        categories = []
        for result in results :
            categories.append(result)

        if request.method == 'POST' and 'category' in request.select :
            cat = request.select['category']
        with closing(conn.cursor()) as c :
            c.execute('select * from Books where category=?',(cat))
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
        bookList=[]
        for result in results:
            bookList.append(result)
    return render_template('books.html',bookList=bookList,books=False)


@app.route('/register')
def register():
    return render_template('register.html',register=True)