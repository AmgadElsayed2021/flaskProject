# flaskProject
i am creating a book store website .
in the header of the web site you will find a photo that represent the bookstore logo

in the main page you will find a navigation bar with home ,categories , books ,(register ,login,logout )buttons depend on the login status.
home will only has a welcome message  and some informations.
categories will have data for each category and a button to see all the books insdide this category.
books will display all the books in the book store with a link to add and a link to delete books.
the add a book link will allow you to add a new book by entering the required data.
the delete a book link will allow you to delete a book by title.

lets go for the coding part
i have divided my project into 2 parts
Application Part and Venv Part
in the Application you will find the below :
Static folder contains 4 folder: - css folder that has a css file to style the website.
                                 - image folder that includes all the images for the books.
                                 - audio folder that include the music file for the website.
                                 - js folder that includes all the js folder to validate the registration form.
                                 
templates folder  contains :-    - includes folder where i add 2 files for the nav and footer of the web site which will be extended in all pages.
                                 -books.html  file where i will display all the books.also will have links to add and delete books
                                 -categories.html file where i will display all the categories also will have links to move to and display the categories.
                                 -categoryBooks.html file where i will display all the books of the selected category.
                                 -delete.html where the user will be able to delete books using the book title.
                                 - update,html file will have a form to upload a new book.
                                 -index.html file that will represent the home page.
                                 -layout.html where i will extend the header andextend the footer page from the includes folder .and that will be extended in all pages.
                                 - login.html file that contains a form that will search the data base and confirm if the user credentials are accurate or not.
                                 - register.html file where new users will be able to create a new user credentials.
                                 -init.py where i will import thr routes.
                                 - forms.py that has the login frame for the login form and the validation method for each input.
                                 - routes.py that has all the routes and the code that is responsiple for each function related to each route also has
                                 the connection to the data base.
                                
Venv folder contains      :-    -app.py just importing the App from the Application folder to do all the running in the venv.
                                - config.py  include a secret key
                                - library.sqlite  data base that contains all the data for the website.
                                -requirements .txt file that contains all the required libraries to run the website.
                                
                                 
