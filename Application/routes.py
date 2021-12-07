import os
import sqlite3
from Application import app
from flask import render_template, request, session, redirect
from contextlib import closing

# def get_db_connection():
conn = sqlite3.connect('database.sqlite', check_same_thread=False)
conn.row_factory = sqlite3.Row
app.config['UPLOAD_PATH']='Application/static/images'

@app.route('/')
@app.route('/home')
@app.route('/index')
def index() :
    return render_template('index.html',
                           index=True)  # just make the index = true so i can use to style the nav button in the nav.html


@app.route('/login', methods=['GET', 'POST'])
def login() :
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


@app.route('/categoryBooks', methods=['GET', 'POST'])
def categoryBooks() :
    category = request.args.get('category')
    with closing(conn.cursor()) as c :
        c.execute('select * from Books where category=?', (category,))
        results = c.fetchall()
        Books = []
        for result in results :
            Books.append(result)
    return render_template("categoryBooks.html", Books=Books, category={"category" : category})


@app.route('/categories', methods=['GET', 'POST'])
def categories() :
    # images=['murach java.png','pacific.jpg']
    with closing(conn.cursor()) as c :
        query = 'select distinct  category ,count(*) as nOfBooks from Books group by category'
        c.execute(query)
        results = c.fetchall()
        categoryList = []
        for result in results :
            categoryList.append(result)
    return render_template('categories.html', categoryList=categoryList, categories=False)


@app.route('/books')
def books() :
    # images=['murach java.png','pacific.jpg']
    with closing(conn.cursor()) as c :
        query = 'select * from Books'
        c.execute(query)
        results = c.fetchall()
        bookList = []
        for result in results :
            bookList.append(result)
    return render_template('books.html', bookList=bookList, books=False)



# below is where the registration routes will be coded
@app.route('/register' )
def register() :
    return render_template('register.html')
@app.route('/registered' )
def registered() :
    return render_template('registered.html')

@app.route('/register',methods =['POST','GET'])
def getRegistrationFormData():
    fname = request.values['fname']
    lname = request.values['lname']
    email = request.values['email']
    password = request.values['password']
    with closing(conn.cursor()) as c :
        c.execute('INSERT INTO Accounts VALUES (?,?,?,?);', (lname, fname, email, password,))
    return redirect('registered')


# below is where i will create the update link
@app.route('/update')
def update():
    return render_template('update.html')
@app.route('/update',methods =['POST','GET'])
def getFormData():
    title=request.values['title']
    year=request.values['year']
    description=request.values['description']
    category =request.values['category']
    uploaded_file=request.files['file']

    if uploaded_file.filename !='':
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'],uploaded_file.filename))
        with closing(conn.cursor())as c:
            c.execute('INSERT INTO Books (Title,Description,Year,Image,Category) VALUES (?,?,?,?,?);', (title, description, year, uploaded_file.filename,category))
    return redirect ('books')


@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/delete',methods =['POST','GET'])
def getDeletedData():
    title=request.values['title']
    with closing(conn.cursor())as c:
        c.execute('Delete from Books where Title=? ;', (title,))
    return redirect ('books')