from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField , BooleanField
from wtforms.validators import DataRequired
# create the login form down here
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password" , validators=[DataRequired()])
    # remember_me = BooleanField("remember me")
    submit = SubmitField("login")
# class RegisterForm(FlaskForm):
#     pass
