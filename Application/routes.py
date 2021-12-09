import os
import sqlite3
from Application import app
from Application.forms import LoginForm
from flask import render_template, request, session, redirect, flash, current_app, abort, url_for
from contextlib import closing
import os

app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif', '.jpeg', '.jfif']

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
    if session.get("email"):
        return redirect(url_for('index'))
    return render_template('index.html')

# here is the route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login() :
    if session.get("email"):
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit() :
        if request.method == 'POST' and 'email' in request.form and 'password' in request.form :
            email = request.form['email']
            password = request.form['password']
            with closing(conn.cursor()) as c :
                c.execute('SELECT * FROM Accounts WHERE email = ? AND password = ?', (email, password,))
                account = c.fetchone()

            if account :
                session['loggedin'] = True
                session['password'] = account['password']
                session['email'] = account['email']

                # use flash and bootstrap to display a message with success style
                flash(f'you are successfully logged in!', "success")
                return redirect('index')
            else :
                # use flash and bootstrap to display a message  with danger style
                flash("sorry : something went wrong.", "danger")
    return render_template('login.html', title="Login", form=form, login=False)

@app.route("/logout")
def logout():
    session['email']=False
    session.pop('email',None)
    return redirect(url_for('index'))





# route for category books
@app.route('/categoryBooks', methods=['GET', 'POST'])
def categoryBooks() :
    if not session.get("email"):
        return redirect(url_for('login'))
    email=session.get['email']
    # query to search the data base for all the available books for a specific category
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
    #  query the data base to get all the categories
    with closing(conn.cursor()) as c :
        c.execute("SELECT DISTINCT  category ,COUNT (*) AS nOfBooks FROM Books GROUP BY category")
        results = c.fetchall()
        categoryList = []
        for result in results :
            categoryList.append(result)
    return render_template('categories.html', categoryList=categoryList, categories=False)


@app.route('/books')
def books() :
    # query the database for all the books that is available in it
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
    if session.get("email"):
        return redirect(url_for('index'))
    return render_template('register.html')


@app.route('/register', methods=['POST', 'GET'])
def getRegistrationFormData() :
    # get the information that is given through the registration form
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
    #  get all the data from the update books form and add them to the data base
    title = request.values['title']
    year = request.values['year']
    description = request.values['description']
    category = request.values['category']
    uploaded_file = request.files['file']
    # check if the uploaded file match the specific requirement we set on top of this routes.py
    if uploaded_file.filename != '' :
        file_ext = os.path.splitext(uploaded_file.filename)[1]
        if file_ext not in current_app.config['UPLOAD_EXTENSIONS'] :
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], uploaded_file.filename))
        # now lets add all those data to the data base
        with closing(conn.cursor()) as c :
            c.execute('INSERT INTO Books (Title,Description,Year,Image,Category) VALUES (?,?,?,?,?);',
                      (title, description, year, uploaded_file.filename, category))
            conn.commit()
    return redirect('books')



#  code the deleting route below here

@app.route('/delete')
def delete() :
    return render_template('delete.html')


@app.route('/delete', methods=['POST', 'GET'])
def getDeletedData() :
    # get the book title from the delete book form and use this in a query to delete that book from the data base
    title = request.values['title']
    with closing(conn.cursor()) as c :
        c.execute('Delete from Books where Title=? ;', (title,))
        conn.commit()
    return redirect('books')
