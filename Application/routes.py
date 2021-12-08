import os
import sqlite3
from Application import app
from Application.forms import LoginForm
from flask import render_template, request, session, redirect, flash
from contextlib import closing
import os

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# def get_db_connection():
conn = sqlite3.connect('library.sqlite', check_same_thread=False)
conn.row_factory = sqlite3.Row
app.config['UPLOAD_PATH'] = 'Application/static/images'


@app.route('/')
@app.route('/home')
@app.route('/index')
def index() :
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login() :
    form = LoginForm()
    if form.validate_on_submit() :
        if request.method == 'POST' and 'email' in request.form and 'password' in request.form :
            email = request.form['email']
            password = request.form['password']
            with closing(conn.cursor()) as c :
                c.execute('SELECT * FROM accounts WHERE email = ? AND password = ?', (email, password,))
                account = c.fetchone()

            if account :
                session['loggedin'] = True
                session['password'] = account['password']
                session['email'] = account['email']

                # use flash and bootstrap to display a message with success style
                flash(f'you are successfully logged in!',"success")
                return redirect('index')
            else :
                # use flash and bootstrap to display a message  with danger style
                flash("sorry : something went wrong.","danger")
    return render_template('login.html', title="Login", form=form, login=True)


@app.route('/categoryBooks', methods=['GET', 'POST'])
def categoryBooks() :
    category = request.args.get('category')
    with closing(conn.cursor()) as c :
        c.execute("SELECT  * FROM Books WHERE category=?", (category,))
        results = c.fetchall()
        Books = []
        for result in results :
            Books.append(result)
    return render_template("categoryBooks.html", Books=Books, category={"category" : category})


@app.route('/categories', methods=['GET', 'POST'])
def categories() :
    # images=['murach java.png','pacific.jpg']
    with closing(conn.cursor()) as c :
        c.execute("SELECT DISTINCT  category ,COUNT (*) AS nOfBooks FROM Books GROUP BY category")
        results = c.fetchall()
        categoryList = []
        for result in results :
            categoryList.append(result)
    return render_template('categories.html', categoryList=categoryList, categories=False)


@app.route('/books')
def books() :
    # images=['murach java.png','pacific.jpg']
    with closing(conn.cursor()) as c :
        c.execute("SELECT * FROM Books")
        results = c.fetchall()
        bookList = []
        for result in results :
            bookList.append(result)
    return render_template('books.html', bookList=bookList, books=False)


# below is where the registration routes will be coded
@app.route('/register')
def register() :
    return render_template('register.html')


@app.route('/register', methods=['POST', 'GET'])
def getRegistrationFormData() :
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    password = request.form['password']
    with closing(conn.cursor()) as c :
        c.execute('INSERT INTO Accounts (fname,lname,email,password) VALUES (?,?,?,?);',
                  (lname, fname, email, password,))
        conn.commit()
    return redirect('login')


# below is where i will create the update link
@app.route('/update')
def update() :
    return render_template('update.html')


@app.route('/update', methods=['POST', 'GET'])
def getFormData() :
    title = request.values['title']
    year = request.values['year']
    description = request.values['description']
    category = request.values['category']
    uploaded_file = request.files['file']

    if uploaded_file.filename != '' :
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], uploaded_file.filename))
        with closing(conn.cursor()) as c :
            c.execute('INSERT INTO Books (Title,Description,Year,Image,Category) VALUES (?,?,?,?,?);',
                      (title, description, year, uploaded_file.filename, category))
            conn.commit()
    return redirect('books')


@app.route('/delete')
def delete() :
    return render_template('delete.html')


@app.route('/delete', methods=['POST', 'GET'])
def getDeletedData() :
    title = request.values['title']
    with closing(conn.cursor()) as c :
        c.execute('Delete from Books where Title=? ;', (title,))
        conn.commit()
    return redirect('books')
