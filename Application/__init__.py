# here is where the application will run
from flask import Flask, render_template
from config import Config

app = Flask(__name__)
# lets import all the routes from the route.html
from Application import routes
# app.config['DEBUG'] = True



# if __name__ == '__main__':
#     app.run(host="localhost", port=8000, debug=True)
