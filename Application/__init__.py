# here is where the application will run
from flask import Flask, render_template

app = Flask(__name__)
# lets import all the routes from the route.html
from Application import routes

